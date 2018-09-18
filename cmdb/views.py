# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics

from .models import HostBasicInfo
from .serializers import HostBasicInfoModelSerializer


class HostBasicInfoList(generics.ListCreateAPIView):
    queryset = HostBasicInfo.objects.all()
    serializer_class = HostBasicInfoModelSerializer


class HostBasicInfoFetchOne(generics.ListAPIView):
    serializer_class = HostBasicInfoModelSerializer

    def get_queryset(self):
        queryset = HostBasicInfo.objects.all()
        ip = self.request.query_params.get("ipaddress", None)
        if ip is not None:
            queryset = HostBasicInfo.objects.filter(ipaddress=ip)
        return queryset


class HostBasicInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HostBasicInfo.objects.all()
    serializer_class = HostBasicInfoModelSerializer

