from django.urls import path
from django.http import HttpResponse

from main.views import show_main, show_experience, show_education, show_project, create_project, get_projects_json, delete_project, create_experience, create_education


app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_education, name="show_education"),
    path("project/", show_project, name="show_project"),
    path("project/add/", create_project, name="create_project"),
    path("experience/add/", create_experience, name="create_experience"),
    path("education/add/", create_education, name="create_education"),
    path("api/project/", get_projects_json, name="get_projects_json"),
    path("project/<uuid:project_id>/delete/",delete_project,name="delete_project")
]
