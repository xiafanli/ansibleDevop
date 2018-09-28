import  requests
import subprocess
import json
import re
from decimal import *

from cmdb.common.field import HostInfoFields


class HostInfoCollect(object):
    STR_PHYSICAL = 'physical'
    STR_VM = 'virtual'
    STR_VM_FLAG = 'VMware'
    HEADERS = {'content-type': 'application/json'}
    REST_URL = 'http://10.0.0.254:8080/cmdb/%s'

    def __init__(self):
        self.ip_exp = re.compile(u'10(\.(2(5[0-5]{1}|[0-4]\d{1})|[0-1]?\d{1,2})){3}')

    def exec_cmd(self, cmd):
        output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return output.communicate()[0]

    def get_hostname(self):
        hostname = self.exec_cmd('hostname').strip()
        return hostname

    def get_cpu(self):
        cpu_num = self.exec_cmd('grep processor /proc/cpuinfo | wc -l')
        return cpu_num

    def get_memory(self):
        memsize = self.exec_cmd("free -g | grep Mem | awk '{print $2}'")
        return memsize

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

    def create_push_data(self):
        host_name = self.get_hostname()
        cpu_num = self.get_cpu()
        mem_num = self.get_memory()
        serial_no = self.get_serial_no()
        ip_address = self.get_ip_address()
        machine_type = self.get_machine_type(serial_no)

        data = {
            HostInfoFields.F_HOST_NAME: host_name,
            HostInfoFields.F_HOST_IP: ip_address,
            HostInfoFields.F_NUM_CPU: cpu_num,
            HostInfoFields.F_NUM_MEM: mem_num,
            HostInfoFields.F_SERIAL_NO: serial_no,
            HostInfoFields.F_MACHINE_TYPE: machine_type,
        }

        return data

    def push_host_info(self):
        ip_address = self.get_ip_address()
        get_request_url = self.REST_URL % ('hosts?ip=%s' % ip_address)
        post_request_url = self.REST_URL % 'hosts'

        data = self.create_push_data()

        try:
            result = requests.get(get_request_url)
            if result.status_code == 200:
                json_result = json.loads(result.content)
                if len(json_result) == 0:
                    post_result = requests.post(post_request_url, data=json.dumps(data), headers=self.HEADERS)
                    print(post_result.status_code)

                else:
                    host_id = json_result[0][HostInfoFields.F_HOST_ID]
                    put_request_url = self.REST_URL % ('hosts/%s' % host_id)
                    put_result = requests.put(put_request_url, data=json.dumps(data), headers=self.HEADERS)
                    print(put_result.status_code)

        except Exception as ex:
            print(ex.__str__())


def main():
    host_collect = HostInfoCollect()
    host_collect.push_host_info()


if __name__ == "__main__":
    main()


# def main():
#     # Frist get all server info value
#     hostname = runCommand('hostname').strip()
#     ip = ip_exp.search(runCommand('ifconfig')).group()
#     cpunum = runCommand('more /proc/cpuinfo  |grep process |wc -l').strip()
#     memnum = Decimal(int(runCommand("more /proc/meminfo  |grep MemTotal |awk '{print $2}'"))/1024/1024)
#     serial = runCommand("dmidecode -t 1 |grep 'Serial Number'|awk -F: '{print $2}'").strip()
#     if serial.startswith('VMware') or serial == '0':
#         server_type = 'virtual'
#         data = {
#              "hostname": hostname,
#              "ipaddress": ip,
#              "numcpu": cpunum,
#              "nummem": str(memnum),
#              "server_type": server_type}
#     else:
#         server_type = 'physical'
#         data = {
#              "hostname": hostname,
#              "ipaddress": ip,
#              "serial": serial,
#              "numcpu": cpunum,
#              "nummem": str(memnum),
#              "server_type": server_type}
#     print(data)
#     # fetch from ip
#     url = 'http://10.0.0.254:8888/api/'
#     request = requests.get(url + 'fetch/?ipaddress=' + ip)
#     if len(json.loads(request.content)) == 0:
#         print("step1")
#         requests.post(url, data=json.dumps(data), headers=headers)
#     else:
#         print("step 2")
#         pk = json.loads(request.content)[0]['id']
#         requests.put(url + str(pk) + "/", headers=headers, data=json.dumps(data))
#

