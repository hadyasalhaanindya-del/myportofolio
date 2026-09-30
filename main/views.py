from django.shortcuts import get_object_or_404, redirect, render

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, JsonResponse
import datetime

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required  
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_POST       

from main.models import Experience, Education, Project
from main.forms import ProjectForm, EducationForm, ExperienceForm



def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Hadya",
        "npm": "2506620406",
        "study_program": "Information System - Undergraduate",
        "bio": (
            "I'm Hadyasalha Alina Anindya, currently majoring in Information System. "
            "Socializing, public speaking, and critical thinking are areas I excel in with confidence. "
            "A full-time eager learner of  mathematics, business management, and programming. "
            
        ),
        "last_login": last_login,
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
        "form": ProjectForm(),
    }
    return render(request, "project.html", context)

#create

@login_required(login_url="/login/")
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
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ProjectForm(request.POST or None)
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
    projects = Project.objects.prefetch_related('starred_by').all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "project_url": project.project_url,
                "project_image_url": project.project_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

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

#register
def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login_user")

    context = {
        "name": "Hadya",
        "form": form,
    }
    return render(request, "register.html", context)

#login
def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Hadya",
        "form": form,
    }
    return render(request, "login.html", context)

#logout
def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

#star
@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")

@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Proyek berhasil ditambahkan.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)