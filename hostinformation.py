import  requests
import subprocess
import json


def runCommand(cmd):
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)


def postData(data)
    url = 'http://10.0.0.254:8888/apid3/'
    headers = {'content-type': 'application/json'}
    requests.post(url, data=json.dumps(data), headers=headers)

data = {
    "hostname": "master2",
    "ipaddress": "10.0.0.111",
    "serial": "J3DKJ",
    "rack_id": "B404",
    "numcpu": "48",
    "nummem": "256",
    "server_type": "physical"
}

requests.post(url, data=json.dumps(data), headers=headers)
