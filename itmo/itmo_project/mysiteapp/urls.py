from django.urls import re_path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
]