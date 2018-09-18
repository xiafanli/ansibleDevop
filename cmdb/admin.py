# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import HostBasicInfo, ClusterBasicInfo, CLusterHostMapping


# Register your models here.


class HostBasicInfoAdmin(admin.ModelAdmin):
    list_display = [
        "hostname",
        "ipaddress",
        "serial",
        "rack_id",
        "numcpu",
        "nummem",
        "server_type"
    ]


admin.site.register(HostBasicInfo, HostBasicInfoAdmin)


class ClusterInfoAdmin(admin.StackedInline):
    model = CLusterHostMapping
    extra = 0


@admin.register(ClusterBasicInfo)
class ClusterBasicInfoAdmin(admin.ModelAdmin):
    inlines = (ClusterInfoAdmin,)
    list_display = [
        'cluster_id',
        'cluster_name',
        'cluster_type',
        'cluster_version'
    ]
