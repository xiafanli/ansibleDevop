from rest_framework import serializers
from .models import ServerInfo


class ServerInfoSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField(read_only=True)
    """
    this is Serializer class
    """
    hostname = serializers.CharField(required=True, allow_blank=False, max_length=30)
    ipaddress = serializers.CharField(required=True, allow_blank=False, max_length=16)
    serial = serializers.CharField(required=False, allow_blank=True)
    rack_id = serializers.CharField(required=False, allow_blank=True)
    numcpu = serializers.CharField(required=True, allow_blank=False)
    nummem = serializers.CharField(required=True, allow_blank=False)
    server_type = serializers.ChoiceField(choices=[('physical', 'physical'), ('virtual', 'virtual')], required=True, allow_blank=False)


class ServerInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerInfo
        fields = (
            'id',
            'hostname',
            'ipaddress',
            'serial',
            'rack_id',
            'numcpu',
            'nummem',
            'server_type',
        )

    # def create(self, validated_date):
    #     """
    #     Create and return a Serverinfo instance
    #     :param validated_date:
    #     :return:
    #     """
    #     print(validated_date)
    #     return ServerInfo.objects.create(**validated_date)
    #
    # def update(self, instance, validated_date):
    #     """
    #     Update and return and exsiting instance 'Serverinfo instance'
    #     """
    #     instance.hostname = validated_date.get('hostanme', instance.hostname)
    #     instance.ipaddress = validated_date.get('ipaddress', instance.ipaddress)
    #     instance.serial = validated_date.get('serial', instance.serial)
    #     instance.rack_id = validated_date.get('rack_id', instance.rack_id)
    #     instance.numcpu = validated_date.get('numcpu', instance.numcpu)
    #     instance.nummem = validated_date.get('nummem', instance.nummem)
    #     instance.server_type = validated_date.get('server_type', instance.server_type)
    #     instance.save()
    #     return instance