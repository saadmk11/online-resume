from django.conf.urls import url

from .views import (
    cv_detail_view, 
    create_personal_info, 
    update_personal_info,
    create_work_experience,
    create_education,
    update_work_experience,
    update_education,
    delete_work_experience,
    delete_education,
    )

urlpatterns = [
    url(r'^create/personal_info$', create_personal_info, name='create_personal_info'), 
    url(r'^update/personal_info/(?P<pk>\d+)/$', update_personal_info, name='update_personal_info'), 
    url(r'^create/work_experience$', create_work_experience, name='create_work_experience'), 
    url(r'^update/work_experience/(?P<pk>\d+)/$', update_work_experience, name='update_work_experience'), 
    url(r'^delete/work_experience/(?P<pk>\d+)/$', delete_work_experience, name='delete_work_experience'),
    url(r'^create/education$', create_education, name='create_education'),
    url(r'^update/education/(?P<pk>\d+)/$', update_education, name='update_education'),  
    url(r'^delete/education/(?P<pk>\d+)/$', delete_education, name='delete_education'), 
    url(r'^(?P<username>\w+)/$', cv_detail_view, name='cv_detail'),
    
]