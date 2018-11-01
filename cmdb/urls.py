from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    #url(r'^$', views.index),
    url('clusters/detail/(?P<pk>[0-9]+)[/]?$', views.ClusterDetailsInfo.as_view()),
    url('clusters/(?P<pk>[0-9]+)[/]?$', views.ClusterInfoRUD.as_view()),
    url('clusters[/]?$', views.ClusterInfo.as_view()),
    url('hosts/(?P<pk>[0-9]+)[/]?', views.HostInfo.as_view()),
    url('hosts[/]?', views.HostInfo.as_view()),
    url('clusterhost[/]?', views.ClusterIpMappingOp.as_view()),
    url('componenthost[/]?', views.ComponentIpMappingOp.as_view()),
    url('components[/]?', views.ComponentInfoList.as_view()),
]