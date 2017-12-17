from django.contrib import admin

from .models import PersonalInfo, WorkExperience, Education
# Register your models here.

admin.site.register(PersonalInfo)
admin.site.register(WorkExperience)
admin.site.register(Education)
