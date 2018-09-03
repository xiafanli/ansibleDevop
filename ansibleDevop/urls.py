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

from cmdb.views import *

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from cmdb.views import serverinfo_list,serverinfo_detail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # """
    # the following three lines in use for the login page
    # """
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^login$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout$', auth_views.logout, {'template_name': 'login.html'}, name='logout'),
    # """
    # the following two lines is use for restful interface demo2
    # """
    url(r'^apid2/$', serverinfo_list),
    url('^apid2/(?P<pk>[0-9]+)/$', serverinfo_detail),
    # """
    # the following two lines is use for restful interface demo3
    # """
    url(r'^apid3/$', ServerinfoListD3.as_view()),
    url('^apid3/(?P<pk>[0-9]+)/$', ServerinfoDetailD3.as_view()),
]
