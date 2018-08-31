# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ServerInfo(models.Model):
    hostname = models.CharField(max_length=30)
    ipaddress = models.CharField(max_length=16)
    serial = models.CharField(max_length=10, default=None)
    rack_id = models.CharField(max_length=10, default=None)
    numcpu = models.CharField(max_length=10, default=None)
    nummem = models.CharField(max_length=10, default=None)
