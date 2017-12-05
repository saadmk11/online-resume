from django import forms
from django.forms.extras.widgets import SelectDateWidget

from .models import PersonalInfo, WorkExperience, Education


class PersonalInfoForm(forms.ModelForm):
    birth_day = forms.DateField(widget=SelectDateWidget(years=range(1940, 2010)))
    class Meta:
        model = PersonalInfo
        fields = (
            "first_name",
            "last_name",
            "tagline",
            "birth_day",
            "gender",
            "nationality",
            "contact_no",
            "email",
            "website",
            "address",
            "country",
            "language",
            "skills",
            "interest",
            "bio",
            "picture",
            )


class WorkExperienceForm(forms.ModelForm):
    joining_year = forms.DateField(widget=SelectDateWidget(years=range(1940, 2018)))
    class Meta:
        model = WorkExperience
        fields = (
            "company_name",
            "job_title",
            "joining_year",
            "job_description",
            )


class EducationForm(forms.ModelForm):
    year = forms.DateField(widget=SelectDateWidget(years=range(1940, 2018)))
    class Meta:
        model = Education
        fields = (
            "institute_name",
            "subject",
            "year",
            "description",
            )
