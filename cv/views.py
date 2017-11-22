from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PersonalInfoForm, WorkExperienceForm, EducationForm
from.models import PersonalInfo, WorkExperience, Education


def cv_detail_view(request, username):
    user = get_object_or_404(User, username=username)
    try:
        personal_info = PersonalInfo.objects.get(user=user)
    except PersonalInfo.DoesNotExist:

        if user == request.user:
            return redirect("create_personal_info") 
        else:    
            raise Http404("CV Does Not Exist.")

    work_experience = WorkExperience.objects.filter(user=user)
    education = Education.objects.filter(user=user)

    context = {
                "personal_info": personal_info,
                "work_experience": work_experience,
                "education": education,
              }

    return render(request, "cv/detail.html", context)


@login_required
def create_personal_info(request):
    try:
        info = PersonalInfo.objects.get(user=request.user)
        raise Http404
    except PersonalInfo.DoesNotExist:
        form = PersonalInfoForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            personal_info = form.save(commit=False)
            personal_info.user = request.user
            personal_info.save()
            return redirect("cv_detail", username=request.user.username) 

        context = {
            "form": form,
        }

        return render(request, "cv/create.html", context)


@login_required
def update_personal_info(request, pk):
    instance = get_object_or_404(PersonalInfo, pk=pk)

    if not request.user == instance.user:
        raise Http404
    else:    
        form = PersonalInfoForm(request.POST or None, request.FILES or None, instance=instance)

        if form.is_valid():
            personal_info = form.save(commit=False)
            personal_info.user = request.user
            personal_info.save()

        context = {
            "form": form,
        }

        return render(request, "cv/create.html", context)


@login_required
def create_work_experience(request):
    form = WorkExperienceForm(request.POST or None)

    if form.is_valid():
        work_experience = form.save(commit=False)
        work_experience.user = request.user
        work_experience.save()
        return redirect("cv_detail", username=request.user.username) 

    context = {
        "form": form,
    }

    return render(request, "cv/create.html", context)


@login_required
def update_work_experience(request, pk):
    instance = get_object_or_404(WorkExperience, pk=pk)

    if not request.user == instance.user:
        raise Http404
    else:    
        form = WorkExperienceForm(request.POST or None, instance=instance)

        if form.is_valid():
            work_experience = form.save(commit=False)
            work_experience.user = request.user
            work_experience.save()
            return redirect("cv_detail", username=request.user.username) 

        context = {
            "form": form,
        }

        return render(request, "cv/create.html", context)


@login_required
def delete_work_experience(request, pk):
    work_experience = get_object_or_404(WorkExperience, pk=pk)

    if not request.user == work_experience.user:
        raise Http404
    else:    
        work_experience.delete()

        return redirect("cv_detail", username=request.user.username) 


@login_required
def create_education(request):
    form = EducationForm(request.POST or None)

    if form.is_valid():
        education = form.save(commit=False)
        education.user = request.user
        education.save()
        return redirect("cv_detail", username=request.user.username) 

    context = {
        "form": form,
    }

    return render(request, "cv/create.html", context)


@login_required
def update_education(request, pk):
    instance = get_object_or_404(Education, pk=pk)

    if not request.user == instance.user:
        raise Http404
    else:    
        form = EducationForm(request.POST or None, instance=instance)

        if form.is_valid():
            education = form.save(commit=False)
            education.user = request.user
            education.save()
            return redirect("cv_detail", username=request.user.username) 

        context = {
            "form": form,
        }

        return render(request, "cv/create.html", context)


@login_required
def delete_education(request, pk):
    education = get_object_or_404(Education, pk=pk)

    if not request.user == education.user:
        raise Http404
    else:    
        education.delete()

        return redirect("cv_detail", username=request.user.username) 
