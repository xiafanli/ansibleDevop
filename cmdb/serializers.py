from rest_framework import serializers
from .models import HostBasicInfo, ClusterBasicInfo


class HostBasicInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostBasicInfo
        fields = (
            'id',
            'hostname',
            'ipaddress',
            'serial',
            'rack_id',
            'numcpu',
            'nummem',
            'server_type',
            'osversion'
        )

class ClusterBasicInfooModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClusterBasicInfo
        fields = (
            'cluster_id',
            'cluster_name',
            'cluster_type',
            'cluster_version'
        )