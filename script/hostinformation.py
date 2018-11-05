import requests
import subprocess
import json
import re
import os
import math
import sys
import glob


from cmdb.common.requestsparam import ComponentHostMapRequestParm
from util.field import HostInfoFields
from util.componetRegexMapping import component_mapping, COMPONENT_LIB_PATH, COMPONENT_LIB_NAME_REGEX

if sys.version < '3':
    reload(sys)
    sys.setdefaultencoding('utf8')

class InfoCollect(object):
    STR_PHYSICAL = 'physical'
    STR_VM = 'virtual'
    STR_VM_FLAG = 'VMware'
    HEADERS = {'content-type': 'application/json'}

    def __init__(self, server_ip, port):
        self.REST_URL = 'http://%s:%s/cmdb/' % (server_ip, port) + '%s'

    def exec_cmd(self, cmd):
        output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return output.communicate()[0].decode()

    def push_host_info(self):
        pass


class HostInfoCollect(InfoCollect):

    def __init__(self, server_ip, port):
        super(HostInfoCollect, self).__init__(server_ip, port)
        self.ip_exp = re.compile(u'10(\.(2(5[0-5]{1}|[0-4]\d{1})|[0-1]?\d{1,2})){3}')
        self.data = {}

    def get_hostname(self):
        super(HostInfoCollect, self)
        hostname = self.exec_cmd('hostname').strip()
        return hostname

    def get_cpu(self):
        cpu_num = self.exec_cmd('grep processor /proc/cpuinfo | wc -l')
        return cpu_num

    def get_memory(self):
        memsize = self.exec_cmd("free -g | grep Mem | awk '{print $2}'")
        canonical_memsize1 = 1 << int(math.ceil(math.log(int(memsize), 2))) - 1
        minus_val = int(memsize) - canonical_memsize1
        canonical_memsize2 = 1 << int(math.ceil(math.log(minus_val, 2)))
        canonical_memsize = canonical_memsize1 + canonical_memsize2
        return canonical_memsize

    def get_serial_no(self):
        serial_no = self.exec_cmd("dmidecode -t 1 |grep 'Serial Number'|awk -F: '{print $2}'").strip()
        return serial_no

    def get_ip_address(self):
        ifconfig_result = self.exec_cmd('ifconfig')
        ip_address = self.ip_exp.search(ifconfig_result).group()
        return ip_address

    def get_machine_type(self, server_no):
        if server_no.startswith(self.STR_VM_FLAG) or server_no == '0':
            machine_type = self.STR_VM
        else:
            machine_type = self.STR_PHYSICAL
        return machine_type

    def get_os_version(self):
        os_version_result = self.exec_cmd("cat /etc/redhat-release")
        return os_version_result

    def create_push_data(self):
        host_name = self.get_hostname()
        cpu_num = self.get_cpu()
        mem_num = self.get_memory()
        serial_no = self.get_serial_no()
        ip_address = self.get_ip_address()
        os_version = self.get_os_version()
        machine_type = self.get_machine_type(serial_no)
        if machine_type == self.STR_VM:
            serial_no = '0'

        self.data = {
            HostInfoFields.F_HOST_NAME: host_name,
            HostInfoFields.F_HOST_IP: ip_address,
            HostInfoFields.F_NUM_CPU: cpu_num,
            HostInfoFields.F_NUM_MEM: mem_num,
            HostInfoFields.F_SERIAL_NO: serial_no,
            HostInfoFields.F_MACHINE_TYPE: machine_type,
            HostInfoFields.F_OS_VERSION: os_version
        }
        return self.data

    def push_host_info(self):
        ip_address = self.get_ip_address()
        get_request_url = self.REST_URL % ('hosts?ip=%s' % ip_address)
        post_request_url = self.REST_URL % 'hosts'

        self.data = self.create_push_data()

        try:
            result = requests.get(get_request_url)
            if result.status_code == 200:
                json_result = result.json()
                if len(json_result) == 0:
                    post_result = requests.post(post_request_url, data=json.dumps(self.data), headers=self.HEADERS)
                    post_result.raise_for_status()
                    print(post_result.status_code)

                else:
                    host_id = json_result[0][HostInfoFields.F_HOST_ID]
                    put_request_url = self.REST_URL % ('hosts/%s' % host_id)
                    put_result = requests.put(put_request_url, data=json.dumps(self.data), headers=self.HEADERS)
                    put_result.raise_for_status()
                    print(put_result.status_code)

        except Exception as ex:
            print(ex.__str__())


class ComponentInfoCollect(InfoCollect):

    def __init__(self, ip, server_ip, port):
        super(ComponentInfoCollect, self).__init__(server_ip, port)
        self.ip = ip
        self.component = self.__get_copmponent_match_result()

    def __get_copmponent_match_result(self):
        result = []
        processes = self.exec_cmd("ps -ef |grep java")
        for process in processes.split("\n"):
            for k, v in component_mapping.items():
                match = re.findall(k, process)
                if len(match) > 0:
                    comp_version = self.get_component_version(v)
                    result.append({ComponentHostMapRequestParm.PARAM_HOST_IP: self.ip,
                                   ComponentHostMapRequestParm.COMPONENT_TYPE: v,
                                   ComponentHostMapRequestParm.COMPONENT_VERSION: comp_version})
        return result

    def exist_path(self, path_name):
        if path_name.find("*") < 0:
            return os.path.exists(path_name)
        else:
            return len(glob.glob(path_name)) > 0


    def get_component_version(self, component_name):
        candidate_paths = COMPONENT_LIB_PATH.get(component_name)
        pattern = re.compile(COMPONENT_LIB_NAME_REGEX.get(component_name))
        for path_str in candidate_paths:
            if self.exist_path(path_str):
                result = self.exec_cmd('ls -1 %s' % path_str)
                ret_list = result.split('\n')
                for filename in ret_list:
                    match_result = pattern.match(filename)
                    if match_result is not None:
                        for version in match_result.groups():
                            if version is not None:
                                return version

        return 'Unknown'

    def push_host_info(self):
        post_request_url = self.REST_URL % 'componenthost'
        data = self.component
        try:
            post_result = requests.post(post_request_url, data=json.dumps(data), headers=self.HEADERS)
            post_result.raise_for_status()
            print(post_result.status_code)
        except Exception as ex:
            print(ex.__str__())


def main(argv):
    if len(argv) < 3:
        print("missing parameter.")
        exit(1)

    server_ip = argv[1]
    port = argv[2]
    host_collect = HostInfoCollect(server_ip, port)
    host_collect.push_host_info()
    ip = host_collect.data[HostInfoFields.F_HOST_IP]
    component_collect = ComponentInfoCollect(ip, server_ip, port)
    component_collect.push_host_info()


if __name__ == "__main__":
    main(sys.argv)
