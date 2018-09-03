# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
# 认证模块
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

from .models import ServerInfo
from .serializers import ServerInfoSerializer

"""
Demo 1 start here
"""
# class ListTodo(generics.ListCreateAPIView):
#     queryset = ServerInfo.objects.all()
#     serializer_class = ServerInfoSerializer

# class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ServerInfo.objects.all()
#     serializer_class = ServerInfoSerializer

"""
Demo 2 start here
"""
@csrf_exempt
def serverinfo_list(request):
    """
    List all server instance or create a new one
    """
    if request.method == 'GET':
        serverinfo = ServerInfo.objects.all()
        serializer = ServerInfoSerializer(serverinfo, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ServerInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def serverinfo_detail(request, pk):
    """
    Retrieve, update or delete a serverinfo object
    """
    try:
        serverinfo = ServerInfo.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ServerInfoSerializer(serverinfo)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ServerInfoSerializer(serverinfo,data=data)
        if serializer.is_valid:
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        serverinfo.delete()
        return HttpResponse(status=204)


class ServerinfoListD3(generics.ListCreateAPIView):
    queryset = ServerInfo.objects.all()
    serializer_class = ServerInfoSerializer


class ServerinfoDetailD3(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServerInfo.objects.all()
    serializer_class = ServerInfoSerializer

