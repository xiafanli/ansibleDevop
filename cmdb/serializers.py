from rest_framework import serializers
from .models import HostBasicInfo


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
