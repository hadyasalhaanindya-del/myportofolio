from django.shortcuts import get_object_or_404, redirect, render



from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse

from main.models import Experience, Education, Project
from main.forms import ProjectForm, EducationForm, ExperienceForm



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
    json_response = get_experience_json(request)
    
    experiences = serializers.deserialize(
            "json",
            json_response.content.decode("utf-8"),
        )
    experiences = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()
    
    context = {
            "name": "Hadya",
            "experience_list": Experience.objects.all(),
            "title_query": title_query,
        }
    return render(request, "experience.html", context)

def show_education(request):
    json_response = get_education_json(request)

    educations = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    educations = [education.object for education in educations]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Hadya",
        "education_list": Education.objects.all(),
        "title_query": title_query,
    }
    return render(request, "education.html", context)


def show_project(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Hadya",
        "project_list": Project.objects.all(),
        "title_query": title_query,
    }
    return render(request, "project.html", context)

#create

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

def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New Education Added!")
        return redirect("main:show_education")

    context = {
        "name": "Hadya",
        "form": form,
    }
    return render(request, "education_form.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New Experience Added!")
        return redirect("main:show_experience")

    context = {
        "name": "Hadya",
        "form": form,
    }
    return render(request, "experience_form.html", context)


#get json

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experience_json = serializers.serialize("json", experiences)
    return HttpResponse(experience_json, content_type="application/json")

def get_education_json(request):
    title_query = request.GET.get("title", "").strip()
    educations = Education.objects.all()

    if title_query:
        educations = educations.filter(title__icontains=title_query)

    education_json = serializers.serialize("json", educations)
    return HttpResponse(education_json, content_type="application/json")


#delete
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project deleted!")
        return redirect("main:show_project")

    return redirect("main:show_project")

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience deleted!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Education deleted!")
        return redirect("main:show_education")

    return redirect("main:show_education")