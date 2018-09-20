# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from .models import HostBasicInfo
from .serializers import HostBasicInfoModelSerializer
from django.http import HttpResponse
from cmdb.models import ClusterBasicInfo
from django.shortcuts import render,render_to_response
import json


#vire interface
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
    print(len(AllclusterObject))
    clusterObjectList = [clusterObject.format() for clusterObject in AllclusterObject]
    return render(request, "manager.html", {"AllclusterObject": AllclusterObject})
    #return render(request, "manager.html", {"clusterObjectList": clusterObjectList})
    #return HttpResponse(json.dumps({"clusterObjectList": clusterObjectList}))


#rest interface
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

