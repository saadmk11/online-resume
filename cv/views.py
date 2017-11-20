from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from.models import PersonalInfo, WorkExperience, Education


def cv_detail_view(request, username):
    user = get_object_or_404(User, username=username)
    try:
        personal_info = PersonalInfo.objects.get(user=user)
    except PersonalInfo.DoesNotExist:
        raise Http404("CV Does Not Exist.")

    work_experience = WorkExperience.objects.filter(user=user)
    education = Education.objects.filter(user=user)

    context = {
                "personal_info": personal_info,
                "work_experience": work_experience,
                "education": education,
              }

    return render(request, "cv/detail.html", context)

    