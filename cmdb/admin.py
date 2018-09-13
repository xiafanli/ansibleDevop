# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ServerInfo


# Register your models here.


class ServerInfoAdmin(admin.ModelAdmin):
    list_display = [
        "hostname",
        "ipaddress",
        "serial",
        "rack_id",
        "numcpu",
        "nummem",
        "server_type"
    ]


admin.site.register(ServerInfo, ServerInfoAdmin)
