# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class ServerInfo(models.Model):
    hostname = models.CharField(max_length=30)
    ipaddress = models.CharField(max_length=16)
    serial = models.CharField(max_length=10, null=True, default="", blank=True)
    rack_id = models.CharField(max_length=10, null=True, default="", blank=True)
    numcpu = models.CharField(max_length=10, default="")
    nummem = models.CharField(max_length=10, default="")
    SERVER_TYPE = [('physical', 'physical'), ('virtual', 'virtual')]
    server_type = models.CharField(max_length=10, choices=SERVER_TYPE, default="physical")
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now_add=True)
    #
    # class Meta:
    #     ordering = ('created',)


class ClusterBasicInfo(models.Model):
    cluster_id = models.IntegerField(primary_key=True)
    cluster_name = models.CharField(max_length=16)
    cluster_type = models.CharField(max_length=30)
    cluster_version = models.CharField(max_length=30,default="", blank=True, null=True)

class CLusterIpMapping(models.Model):
    cluster_id = models.ForeignKey(ClusterBasicInfo, related_name="mapping_basic", on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=16)

