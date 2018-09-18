import  requests
import subprocess
import json
import re
from decimal import *


ip_exp = re.compile(u'10(\.(2(5[0-5]{1}|[0-4]\d{1})|[0-1]?\d{1,2})){3}')
headers = {'content-type': 'application/json'}


def runCommand(cmd):
    output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return output.communicate()[0]


def main():
    # Frist get all server info value
    hostname = runCommand('hostname').strip()
    ip = ip_exp.search(runCommand('ifconfig')).group()
    cpunum = runCommand('more /proc/cpuinfo  |grep process |wc -l').strip()
    memnum = Decimal(int(runCommand("more /proc/meminfo  |grep MemTotal |awk '{print $2}'"))/1024/1024)
    serial = runCommand("dmidecode -t 1 |grep 'Serial Number'|awk -F: '{print $2}'").strip()
    if serial.startswith('VMware') or serial == '0':
        server_type = 'virtual'
        data = {
             "hostname": hostname,
             "ipaddress": ip,
             "numcpu": cpunum,
             "nummem": str(memnum),
             "server_type": server_type}
    else:
        server_type = 'physical'
        data = {
             "hostname": hostname,
             "ipaddress": ip,
             "serial": serial,
             "numcpu": cpunum,
             "nummem": str(memnum),
             "server_type": server_type}
    print(data)
    # fetch from ip
    url = 'http://10.0.0.254:8888/api/'
    request = requests.get(url + 'fetch/?ipaddress=' + ip)
    if len(json.loads(request.content)) == 0:
        print("step1")
        requests.post(url, data=json.dumps(data), headers=headers)
    else:
        print("step 2")
        pk = json.loads(request.content)[0]['id']
        requests.put(url + str(pk) + "/", headers=headers, data=json.dumps(data))


if __name__ == "__main__":
    main()
