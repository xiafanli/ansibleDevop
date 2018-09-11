import  requests
import subprocess
import json
import re
import socket


ip_exp = re.compile(u'10(\.(2(5[0-5]{1}|[0-4]\d{1})|[0-1]?\d{1,2})){3}')


def runCommand(cmd):
    output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return output.communicate()[0]


def postData(url, data):
    headers = {'content-type': 'application/json'}
    request = requests.post(url, data=json.dumps(data), headers=headers)
    return request


data = {
    "hostname": "master2",
    "ipaddress": "10.0.0.111",
    "serial": "J3DKJ",
    "rack_id": "B404",
    "numcpu": "48",
    "nummem": "256",
    "server_type": "physical"
}


def main():
    # Frist get all server info value
    hostname = runCommand("hostname")
    ip = re.search(runCommand("ifconfig"))
    cpunum = runCommand("more /proc/cpuinfo  |grep process |wc -l")
    memnum = runCommand("more /proc/meminfo  |grep process |wc -l")
    serial = runCommand("dmidecode -t 1 |grep Serial number")
    if serial.startswith("VMware"):
        server_type = "virtual"
    else:
        server_type = "physical"
    # fetch from ip
    url = "http://10.0.0.254:8888/apid3/fetch/"
    request = requests.get(url + ip)
    print(request.status_code)
    data = {
        "hostname": hostname,
        "ipaddress": ip,
        "serial": "J3DKJ",
        "rack_id": "B404",
        "numcpu": "48",
        "nummem": "256",
        "server_type": "physical"
    }
