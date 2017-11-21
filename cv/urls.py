from django.conf.urls import url

from .views import cv_detail_view, create_personal_info, update_personal_info

urlpatterns = [
    url(r'^create/personal_info$', create_personal_info, name='create_personal_info'), 
    url(r'^update/personal_info/(?P<pk>\d+)/$', update_personal_info, name='update_personal_info'), 
    url(r'^(?P<username>\w+)/$', cv_detail_view, name='cv_detail'),
    
]