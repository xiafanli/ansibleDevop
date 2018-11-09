# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics, status
from rest_framework.response import Response

from cmdb.common.requestsparam import ClusterHostMapRequestParam,ComponentHostMapRequestParm
from cmdb.common.responsetool import ResponseTool
from util.field import HostInfoFields, ClusterFields
from .models import HostBasicInfo, ClusterHostMapping, ClusterBasicInfo, ComponentInfo, ComponentHostMapping
from .serializers import HostBasicInfoModelSerializer, ClusterHostInfoSerializer, ClusterBasicInfoModelSerializer, \
    ClusterBasicInfoModelCreateSerializer, ComponentInfoSerializer
from django.shortcuts import render
from django.http import JsonResponse
from cmdb.common import options
import json
from django.contrib.auth.decorators import login_required
from cmdb.scheculer.schedulers import JobScheduler
from cmdb.scheculer.schedulers import CollectHostInfo


task_scheduler = JobScheduler()
task_scheduler.add_job(CollectHostInfo(options.IDC_INFO_WEB_SERVER_IP).update_host_info_from_idc, "job1", 60)
task_scheduler.start()

# view interface
@login_required(login_url='/login')
def index(request):
    return render(request, 'index.html')


@login_required(login_url="/login")
def cluster_info(request):
    if request.method == "POST":
        # cluster_id = request.POST['cluster_id']
        cluster_name = request.POST['cluster_name']
        cluster_type = request.POST['cluster_type']
        cluster_version = request.POST['cluster_version']
        ClusterBasicInfo.objects.update_or_create(
            cluster_name=cluster_name,
            cluster_type=cluster_type,
            cluster_version=cluster_version
        )
        # clusterObject.save()
        AllclusterObject = ClusterBasicInfo.objects.all().order_by(ClusterFields.F_CLUSTER_ID)
    else:
        AllclusterObject = ClusterBasicInfo.objects.all().order_by(ClusterFields.F_CLUSTER_ID)
    return render(request, "manager.html", {"AllclusterObject": AllclusterObject,
                                            "cluster_type": options.CLUSTER_TYPE})


@login_required(login_url="/login")
def aggregate_cluster(request):
    cluster_count = {}
    result = []
    host = ClusterHostMapping.objects.all()
    for i in host:
        if i.cluster_info.cluster_name in cluster_count:
            cluster_count[i.cluster_info.cluster_name] += 1
        else:
            cluster_count[i.cluster_info.cluster_name] = 1
    for k, v in cluster_count.items():
        result.append({'name': k, 'value': v})
    return JsonResponse(json.dumps({"result": result}), safe=False)


@login_required(login_url="/login")
def aggregate_componet(request):
    component_count = {}
    result = []
    host = ComponentHostMapping.objects.all()
    for i in host:
        if i.component_info.component_type in component_count:
            component_count[i.component_info.component_type] += 1
        else:
            component_count[i.component_info.component_type] = 1
    for k, v in component_count.items():
        result.append({'name': k, 'value': v})
    return JsonResponse(json.dumps({"result": result}), safe=False)


@login_required(login_url="/login")
def host_info(request):
    AllhostObject = HostBasicInfo.objects.all().order_by(HostInfoFields.F_HOST_IP)
    return render(request, 'host.html', {"AllhostObject": AllhostObject})


@login_required(login_url="/login")
def get_cluster_info_by_ip(request):
    cluster = []
    component = []
    ip = request.POST['ip']
    host_object = HostBasicInfo.objects.filter(ip_address=ip)
    for host in host_object:
        cluster = [info.cluster_info.cluster_name for info in host.host_cluster.all()]
        component = [info.component_info.component_type for info in host.host_component.all()]
    return JsonResponse(json.dumps({'cluster': "\t".join(cluster), 'component': ", ".join(component)}), safe=False)


# rest interface
class HostInfo(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = HostBasicInfo.objects.all()
    serializer_class = HostBasicInfoModelSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        host_ip = request.data[HostInfoFields.F_HOST_IP]
        host_info_queryset = HostBasicInfo.objects.filter(ip_address=host_ip)
        if host_info_queryset.count() > 0:
            return Response(ResponseTool.get_response_data('host ip %s has exist.' % host_ip),
                            status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        queryset = HostBasicInfo.objects.all()
        ip = self.request.query_params.get("ip", None)
        if ip is not None:
            queryset = HostBasicInfo.objects.filter(ip_address=ip)
        return queryset


class ClusterInfo(generics.ListCreateAPIView):
    queryset = ClusterBasicInfo.objects.all()
    serializer_class = ClusterBasicInfoModelSerializer

    def create(self, request, *args, **kwargs):
        self.serializer_class = ClusterBasicInfoModelCreateSerializer
        # cluster_id = request.data[ClusterFields.F_CLUSTER_ID]
        # if self.exist_cluster_id(cluster_id):
        #     return Response(ResponseTool.get_response_data('Cluster id %s has exist.' % cluster_id))

        cluster_name = request.data[ClusterFields.F_CLUSTER_NAME]
        if self.exist_cluster_name(cluster_name):
            return Response(ResponseTool.get_response_data('Cluster name %s has exist.' % cluster_name))

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def exist_cluster_name(self, cluster_name):
        cluster_info_queryset = ClusterBasicInfo.objects.filter(cluster_name=cluster_name)
        if cluster_info_queryset.count() > 0:
            return True
        else:
            return False

    # def exist_cluster_id(self, cluster_id):
    #     cluster_info_queryset = ClusterBasicInfo.objects.filter(cluster_id=cluster_id)
    #     if cluster_info_queryset.count() > 0:
    #         return True
    #     else:
    #         return False


class ClusterInfoRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClusterBasicInfo.objects.all()
    serializer_class = ClusterBasicInfoModelSerializer


class ClusterDetailsInfo(generics.RetrieveAPIView):
    queryset = ClusterBasicInfo.objects.all()
    serializer_class = ClusterHostInfoSerializer


class ComponentInfoList(generics.ListAPIView):
    queryset = ComponentInfo.objects.all()
    serializer_class = ComponentInfoSerializer


class ClusterIpMappingOp(generics.CreateAPIView):

    def create(self, request, *args, **kwargs):
        msg_error = []
        request_data = request.data
        for one_record in request_data:
            (msg, is_success) = self.create_cluster_host_map(one_record)
            if not is_success:
                msg_error.append(msg)

        if len(msg_error) > 0:
            return Response(ResponseTool.get_response_data(msg_error), status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(ResponseTool.get_response_data("Create cluster and host mapping sucessfully"),
                            status=status.HTTP_201_CREATED)

    def create_cluster_host_map(self, one_record):
        host_ip = one_record.get(ClusterHostMapRequestParam.PARAM_HOST_IP)
        if host_ip is None:
            return "Missing parameter host_ip.", False

        cluster_name = one_record.get(ClusterHostMapRequestParam.PARAM_CLUSTER_NAME)
        cluster_id = one_record.get(ClusterHostMapRequestParam.PARAM_CLUSTER_ID)
        if cluster_name is None and cluster_id is None:
            return "must provide one parameter between cluster_name and cluster_id.", False

        if cluster_name is not None:
            cluster_queryset = ClusterBasicInfo.objects.filter(cluster_name=cluster_name)
            if cluster_queryset.count() == 0:
                return "Cluster %s does not exist." % cluster_name, False

        if cluster_id is not None:
            cluster_queryset = ClusterBasicInfo.objects.filter(cluster_id=cluster_id)
            if cluster_queryset.count() == 0:
                return "Cluster id %s does not exist." % cluster_id, False

        host_info_queryset = HostBasicInfo.objects.filter(ip_address=host_ip)
        if host_info_queryset.count() == 0:
            host_info = HostBasicInfo(ip_address=host_ip)
            host_info.save()
            host_info_queryset = HostBasicInfo.objects.filter(ip_address=host_ip)

        mapping_queryset = ClusterHostMapping.objects.filter(cluster_info=cluster_queryset[0],
                                                             host_info=host_info_queryset[0])
        if mapping_queryset.count() > 0:
            return "The mapping of cluster %s and host %s has exist." % \
                   (cluster_name if cluster_name is not None else cluster_id,
                    host_ip), False

        cls_ip_mapping = ClusterHostMapping(cluster_info=cluster_queryset[0], host_info=host_info_queryset[0])
        cls_ip_mapping.save()
        return "Create cluster and host mapping sucessfully.", True


class ComponentIpMappingOp(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        request_data = request.data
        msg_error = []
        for one_item in request_data:
            msg, is_success = self.create_component_host_map(one_item)
            if not is_success:
                msg_error.append(msg)

        if len(msg_error) > 0:
            return Response(ResponseTool.get_response_data(msg_error), status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(ResponseTool.get_response_data("Create or update component and host mapping sucessfully"),
                            status=status.HTTP_201_CREATED)

    def create_component_host_map(self, one_item):
        host_ip = one_item.get(ComponentHostMapRequestParm.PARAM_HOST_IP)
        if host_ip is None:
            return "Missing parameter host_ip.", False
        else:
            host_info_queryset = HostBasicInfo.objects.filter(ip_address=host_ip)

        if host_info_queryset.count() < 1:
            return "host %s doesn't exist" % host_ip, False

        component_type = one_item.get(ComponentHostMapRequestParm.COMPONENT_TYPE)
        component_version = one_item.get(ComponentHostMapRequestParm.COMPONENT_VERSION)

        if len(component_type) == 0:
            return "component not found on the server or type error.", False

        if len(component_version) == 0:
            return "component version is None.", False

        component_queryset = ComponentInfo.objects.get_or_create(component_type=component_type,
                                                                 component_version=component_version)

        comp_host_queryset = ComponentHostMapping.objects.filter(host_info=host_info_queryset[0])

        to_delete_records = []
        exist_record = False
        for comp_host in comp_host_queryset:
            if comp_host.component_info.component_type == component_type:
                if comp_host.component_info.component_version != component_version:
                    to_delete_records.append(comp_host)
                else:
                    exist_record = True

        for comp_host in to_delete_records:
            queryset = ComponentHostMapping.objects.filter(host_info=comp_host.host_info,
                                                           component_info=comp_host.component_info)
            queryset.delete()

        if not exist_record:
            ComponentHostMapping.objects.create(component_info=component_queryset[0],
                                                      host_info=host_info_queryset[0])
            return "create or update host component mapping successfully.", True
        else:
            return "Host component mapping has exist.", True
