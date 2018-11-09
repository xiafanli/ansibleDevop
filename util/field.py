# -*- coding: utf-8 -*-


class HostInfoFields:
    F_HOST_ID = 'id'
    F_HOST_NAME = "host_name"
    F_HOST_IP = 'ip_address'
    F_SERIAL_NO = 'serial'
    F_RACK_ID = 'rack_id'
    F_NUM_CPU = 'num_cpu'
    F_NUM_MEM = 'num_mem'
    F_OS_VERSION = 'os_version'
    F_MACHINE_TYPE = 'machine_type'
    F_HOST_CLUSTER = 'host_cluster'
    F_HOST_COMPNENET = 'host_component'
    F_MANAGER_IP = 'manager_ip'
    F_MODEL = 'model'
    F_ROOM = 'room'


class ClusterFields:
    F_CLUSTER_ID = 'cluster_id'
    F_CLUSTER_NAME = 'cluster_name'
    F_CLUSTER_TYPE = 'cluster_type'
    F_CLUSTER_VERSION = 'cluster_version'
    F_HOST_INFO_LIST = 'host_info_list'


class ClusterHostMapFields:
    F_CLUSTER_INFO = 'cluster_info'
    F_HOST_INFO = 'host_info'


class ComponentHostMapFields:
    F_COMPONENT_HOSTNAME = "host_name"
    F_COMPONENT_IP = "ip_address"
    F_HOST_INFO = "component_info"


class ComponentInfoFields:
    F_COMPONENT_TYPE = 'component_type'
    F_COMPONENT_VERSION = 'component_version'