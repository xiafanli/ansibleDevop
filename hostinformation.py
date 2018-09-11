import  requests
import subprocess
import json
import re


ip_exp = re.compile(u'10(\.(2(5[0-5]{1}|[0-4]\d{1})|[0-1]?\d{1,2})){3}')
headers = {'content-type': 'application/json'}


def runCommand(cmd):
    output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return output.communicate()[0]


def main():
    # Frist get all server info value
    hostname = runCommand('hostname')
    ip = ip_exp.search(runCommand('ifconfig')).group()
    cpunum = runCommand('more /proc/cpuinfo  |grep process |wc -l')
    memnum = int(runCommand("more /proc/meminfo  |grep MemTotal |awk '{print $2}'"))/1024/1024
    serial = runCommand('dmidecode -t 1 |grep Serial Number')
    if serial.startswith('VMware'):
        server_type = 'virtual'
        serial = ''
    else:
        server_type = 'physical'

    data = {
        "hostname": hostname,
        "ipaddress": ip,
        "serial": serial,
        "rack_id": "",
        "numcpu": cpunum,
        "nummem": memnum,
        "server_type": server_type
    }
    print(data)
    # fetch from ip
    url = 'http://10.0.0.254:8888/apid3/'
    request = requests.get(url +  'fetch/?ipaddress='  + ip)
    print(request.status_code)
    if len(json.loads(request.content)) == 0:
        requests.post(url, data=json.dumps(data), headers=headers)
    else:
        print
        pk = json.loads(request.content)[0]['id']
        requests.post(url + pk, headers=headers, data=json.dumps(data))


if __name__ == "__main__":
    main()
