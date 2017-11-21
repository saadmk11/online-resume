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
