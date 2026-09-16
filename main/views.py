from django.shortcuts import get_object_or_404, redirect, render



from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse

from main.models import Experience, Education, Project
from main.forms import ProjectForm



def show_main(request):
    context = {
        "name": "Hadya",
        "npm": "2506620406",
        "study_program": "Information System - Undergraduate",
        "bio": (
            "I'm Hadyasalha Alina Anindya, currently majoring in Information System. "
            "Socializing, public speaking, and critical thinking are areas I excel in with confidence. "
            "A full-time eager learner of  mathematics, business management, and programming. "
            
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Hadya",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    context = {
        "name": "Hadya",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)

def show_project(request):
    context = {
        "name": "Hadya",
        "project_list": Project.objects.all(),
    }
    return render(request, "project.html", context)






def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New Project Added!")
        return redirect("main:show_project")

    context = {
        "name": "Hadya",
        "form": form,
    }
    return render(request, "projects_form.html", context)

    