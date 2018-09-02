# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ServerInfo(models.Model):
    hostname = models.CharField(max_length=30)
    ipaddress = models.CharField(max_length=16)
    serial = models.CharField(max_length=10, default="")
    rack_id = models.CharField(max_length=10, default="")
    numcpu = models.CharField(max_length=10, default="")
    nummem = models.CharField(max_length=10, default="")
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now_add=True)
    #
    # class Meta:
    #     ordering = ('created',)
