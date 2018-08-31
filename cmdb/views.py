# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
# 认证模块
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt


from rest_framework import generics

from .models import ServerInfo
from .serializers import ServerInfoSerializer


class ListTodo(generics.ListCreateAPIView):
    queryset = ServerInfo.objects.all()
    serializer_class = ServerInfoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServerInfo.objects.all()
    serializer_class = ServerInfoSerializer