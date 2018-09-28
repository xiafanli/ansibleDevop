# -*- coding: utf-8 -*-

import sys
import json
import requests


HEADERS = {'content-type': 'application/json'}
REST_URL = 'http://127.0.0.1:8000/cmdb/clusterhost/'


def batch_add_cluster_host(file):
    cluster_host_list = []
    with open(file) as datafile:
        for one_line in datafile:
            tmp_array = one_line.split(',')
            if len(tmp_array) == 2:
                cluster_host_list.append({'host_ip': tmp_array[0], 'cluster_name': tmp_array[1].replace('\n', '')})
            else:
                print("error format: %s " % one_line)

    try:
        result = requests.post(REST_URL, data=json.dumps(cluster_host_list), headers=HEADERS)
        print(result.json())
    except Exception as ex:
        print(ex.__str__())



def main():
    if len(sys.argv) < 2:
        print("missing filename argument.")
        return
    filename = sys.argv[1]
    print(filename)
    batch_add_cluster_host(filename)


if __name__ == '__main__':
    main()
