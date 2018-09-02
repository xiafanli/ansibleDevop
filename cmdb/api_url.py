from django.conf.urls import url
from . import views

from . import views

urlpatterns = [
    url('', views.serverinfo_list),
    url('^(?P<pk>[0-9]+)/$', views.serverinfo_detail),
]