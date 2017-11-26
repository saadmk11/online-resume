from django import forms

from .models import PersonalInfo, WorkExperience, Education


class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = [
            "first_name",
            "last_name",
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
            "bio",
            "picture",
            ]


class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = [
            "company_name",
            "job_title",
            "joining_year",
            "job_description",
            ]


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = [
            "institute_name",
            "subject",
            "year",
            "description",
            ]
