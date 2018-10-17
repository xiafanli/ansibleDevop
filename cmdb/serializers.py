from rest_framework import serializers

from cmdb.common.field import HostInfoFields, ClusterFields, ComponentInfoFields
from .models import HostBasicInfo, ClusterBasicInfo
from .models import ComponentInfo


class HostBasicInfoModelSerializer(serializers.ModelSerializer):
    host_cluster = serializers.SerializerMethodField()

    class Meta:
        model = HostBasicInfo
        fields = (
            HostInfoFields.F_HOST_ID,
            HostInfoFields.F_HOST_NAME,
            HostInfoFields.F_HOST_IP,
            HostInfoFields.F_SERIAL_NO,
            HostInfoFields.F_RACK_ID,
            HostInfoFields.F_NUM_CPU,
            HostInfoFields.F_NUM_MEM,
            HostInfoFields.F_MACHINE_TYPE,
            HostInfoFields.F_OS_VERSION,
            HostInfoFields.F_HOST_CLUSTER,
        )

    def get_host_cluster(self, obj):
        cls = obj.host_cluster.all()
        cluster_names = []
        for c in cls:
            cluster_names.append(c.cluster_info.cluster_name)
        return cluster_names


class ClusterBasicInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClusterBasicInfo
        fields = (
            ClusterFields.F_CLUSTER_ID,
            ClusterFields.F_CLUSTER_NAME,
            ClusterFields.F_CLUSTER_TYPE,
            ClusterFields.F_CLUSTER_VERSION,
        )


class ClusterHostInfoSerializer(serializers.ModelSerializer):
    host_info_list = serializers.SerializerMethodField()

    class Meta:
        model = ClusterBasicInfo
        fields = [
            ClusterFields.F_CLUSTER_ID,
            ClusterFields.F_CLUSTER_NAME,
            ClusterFields.F_CLUSTER_TYPE,
            ClusterFields.F_CLUSTER_VERSION,
            ClusterFields.F_HOST_INFO_LIST,
        ]

    def get_host_info_list(self, obj):
        cls_host_queryset = obj.mapping_basic.all()
        host_list = []
        for cluster_host in cls_host_queryset:
            host_list.append(cluster_host.host_info.to_dict())
        return host_list


class ComponentHostInfoSerializer(serializers.ModelSerializer):
    component_info_list = serializers.SerializerMethodField()

    class Meta:
        model = ComponentInfo
        fields = [
            ComponentInfoFields.F_COMPONENT_TYPE,
            ComponentInfoFields.F_COMPONENT_VERSION,
            ComponentInfoFields.F_HOST_INFO_LIST
        ]
