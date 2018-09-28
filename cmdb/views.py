# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from .serializers import HostBasicInfoModelSerializer
from cmdb.models import *
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import json

# view interface
def ClusterInfoView(request):
    if request.method == "POST":
        cluster_id = request.POST['cluster_id']
        cluster_name = request.POST['cluster_name']
        cluster_type = request.POST['cluster_type']
        cluster_version = request.POST['cluster_version']
        clusterObject = ClusterBasicInfo.objects.create(
            cluster_id=cluster_id,
            cluster_name=cluster_name,
            cluster_type=cluster_type,
            cluster_version=cluster_version
        )
        clusterObject.save()
        AllclusterObject = ClusterBasicInfo.objects.all().order_by("cluster_id")
    else:
        AllclusterObject = ClusterBasicInfo.objects.all().order_by("cluster_id")
    return render(request, "manager.html", {"AllclusterObject": AllclusterObject, "cluster_type": settings.CLUSTER_TYPE})


def HostInfoView(request):
    AllhostObject = HostBasicInfo.objects.all().order_by("ipaddress")
    return render(request, 'host.html', {"AllhostObject": AllhostObject})


def get_cluster_info_by_ip(request):
    cluster = []
    ip = request.POST['ip']
    host_object = HostBasicInfo.objects.filter(ipaddress=ip)
    for host in host_object:
        for info in host.host_cluster.all():
            cluster.append(info.clusterinfo.cluster_name)
    return JsonResponse(json.dumps({'cluster': "\t".join(cluster)}), safe=False)


# rest interface
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

