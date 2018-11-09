from rest_framework import serializers

from util.field import HostInfoFields, ClusterFields, ComponentInfoFields
from .models import HostBasicInfo, ClusterBasicInfo, ComponentInfo


class HostBasicInfoModelSerializer(serializers.ModelSerializer):
    host_cluster = serializers.SerializerMethodField()
    host_component = serializers.SerializerMethodField()

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
            HostInfoFields.F_MANAGER_IP,
            HostInfoFields.F_MODEL,
            HostInfoFields.F_ROOM,
            HostInfoFields.F_HOST_CLUSTER,
            HostInfoFields.F_HOST_COMPNENET,
        )

    def get_host_cluster(self, obj):
        cls = obj.host_cluster.all()
        cluster_names = []
        for c in cls:
            cluster_names.append(c.cluster_info.cluster_name)
        return cluster_names

    def get_host_component(self, obj):
        all_components = obj.host_component.all()
        component_names = []
        for c in all_components:
            component_names.append(c.component_info.to_dict())
        return component_names


class ClusterBasicInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClusterBasicInfo
        fields = (
            ClusterFields.F_CLUSTER_ID,
            ClusterFields.F_CLUSTER_NAME,
            ClusterFields.F_CLUSTER_TYPE,
            ClusterFields.F_CLUSTER_VERSION,
        )


class ClusterBasicInfoModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClusterBasicInfo
        fields = (
            ClusterFields.F_CLUSTER_NAME,
            ClusterFields.F_CLUSTER_TYPE,
            ClusterFields.F_CLUSTER_VERSION,
        )


class ComponentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentInfo
        fields = (
            ComponentInfoFields.F_COMPONENT_TYPE,
            ComponentInfoFields.F_COMPONENT_VERSION,
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
            host_comp_queryset = cluster_host.host_info.host_component.all()
            host_info_dict = cluster_host.host_info.to_dict()
            host_components = []
            for host_comp in host_comp_queryset:
                host_components.append(host_comp.component_info.to_dict())

            host_info_dict.update({HostInfoFields.F_HOST_COMPNENET: host_components})
            host_list.append(host_info_dict)
        return host_list


