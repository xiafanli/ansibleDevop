from django.conf.urls import url
from . import views

from . import views

urlpatterns = [
    url('', views.ListTodo.as_view()),
    url('<string:pk>/', views.DetailTodo.as_view()),
]