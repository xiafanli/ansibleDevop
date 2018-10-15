# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class HostBasicInfo(models.Model):
    host_name = models.CharField(max_length=30,  null=True, default="", blank=True)
    ip_address = models.CharField(max_length=16)
    serial = models.CharField(max_length=10, null=True, default="", blank=True)
    rack_id = models.CharField(max_length=10, null=True, default="", blank=True)
    num_cpu = models.CharField(max_length=10, default="")
    num_mem = models.CharField(max_length=10, default="")
    os_version = models.CharField(max_length=30, null=True, default="", blank=True)
    SERVER_TYPE = [('physical', 'physical'), ('virtual', 'virtual')]
    machine_type = models.CharField(max_length=10, choices=SERVER_TYPE, default="physical")

    def to_dict(self):
        host_dict = {
            "host_name": self.host_name,
            "ip_address": self.ip_address,
            "serial": self.serial,
            "rack_id": self.rack_id,
            "num_cpu": self.num_cpu,
            "num_mem": self.num_mem,
            "os_version": self.os_version,
            "machine_type": self.machine_type
        }
        return host_dict


class ClusterBasicInfo(models.Model):
    cluster_id = models.IntegerField(primary_key=True)
    cluster_name = models.CharField(max_length=16)
    cluster_type = models.CharField(max_length=30)
    cluster_version = models.CharField(max_length=30, default="", blank=True, null=True)
    host_info = models.ManyToManyField(HostBasicInfo, through="ClusterHostMapping")


class ClusterHostMapping(models.Model):
    cluster_info = models.ForeignKey(ClusterBasicInfo, related_name="mapping_basic", on_delete=models.CASCADE)
    host_info = models.ForeignKey(HostBasicInfo, related_name="host_cluster", on_delete=models.CASCADE)


class ComponentInfo(models.Model):
    component_type = models.CharField(max_length=30)
    component_version = models.CharField(max_length=30)
    host_info = models.ManyToManyField(HostBasicInfo, through="ComponentHostMapping")


class ComponentHostMapping(models.Model):
    component_info = models.ForeignKey(ComponentInfo, on_delete=models.CASCADE)
    host_info = models.ForeignKey(HostBasicInfo, on_delete=models.CASCADE)
