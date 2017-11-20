from django.conf.urls import url

from .views import cv_detail_view

urlpatterns = [
    url(r'^(?P<username>\w+)/$', cv_detail_view, name='cv_detail'),

]