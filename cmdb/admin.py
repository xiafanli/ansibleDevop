# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import HostBasicInfo, ClusterBasicInfo, ClusterHostMapping, ComponentInfo


# Register your models here.


class HostBasicInfoAdmin(admin.ModelAdmin):
    list_display = [
        "host_name",
        "ip_address",
        "serial",
        "rack_id",
        "num_cpu",
        "num_mem",
        "machine_type",
        "os_version"
    ]


admin.site.register(HostBasicInfo, HostBasicInfoAdmin)


class ClusterInfoAdmin(admin.StackedInline):
    model = ClusterHostMapping
    extra = 0


@admin.register(ClusterBasicInfo)
class ClusterBasicInfoAdmin(admin.ModelAdmin):
    inlines = (ClusterInfoAdmin,)
    list_display = [
        'cluster_name',
        'cluster_type',
        'cluster_version'
    ]


@admin.register(ComponentInfo)
class ComponentInfoAdmin(admin.ModelAdmin):

    list_display = [
        'component_type',
        'component_version'
    ]