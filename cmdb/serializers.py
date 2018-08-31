from rest_framework import serializers
from .models import ServerInfo


class ServerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'hostname',
            'ipaddress',
            'serial',
            'rack_id',
            'numcpu',
            'nummem',
        )
        model = ServerInfo

