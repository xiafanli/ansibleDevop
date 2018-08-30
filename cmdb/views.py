# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import render

# Create your views here.
def index(request):
    return render_to_response("index.html")
