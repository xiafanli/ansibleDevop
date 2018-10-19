"""ansibleDevop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, path

from cmdb.views import *
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from cmdb.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # """
    # the following three lines in use for the login page
    # """
    url(r'^$',index, name='home'),
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^logout$', LogoutView.as_view(), name='logout'),
    url(r'^cluster$', cluster_info, name='cluster'),
    url(r'^host', host_info, name='cluster'),
    url(r'^getclusterinfo$', get_cluster_info_by_ip, name='getclusterinfo'),
    url(r'^aggregatecluster$', aggregate_cluster, name='aggregatecluster'),
    url(r'^aggregatecomponent$', aggregate_componet, name='aggregatecomponent$'),
    # """
    # the following two lines is use for restful interface
    # """
    path('cmdb/', include('cmdb.urls'))
]
