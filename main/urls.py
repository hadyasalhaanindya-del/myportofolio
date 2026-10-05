from django.urls import path
from django.http import HttpResponse
from main.views import (
    show_main,
    show_experience,
    show_education,
    show_project,
    create_project,
    get_projects_json,
    delete_project,
    delete_education,
    delete_experience,
    create_experience,
    create_education,
    get_education_json,
    get_experience_json,
    login_user,
    logout_user,
    register,
    toggle_star,
    create_project_ajax,
    create_education_ajax,
    create_experience_ajax,
)


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
    path("api/education/", get_education_json, name="get_education_json"),
    path("api/project/", get_experience_json, name="get_experience_json"),
    path("project/<uuid:project_id>/delete/",delete_project,name="delete_project"),
    path("education/<uuid:education_id>/delete/",delete_education,name="delete_education"),
    path("experience/<uuid:experience_id>/delete/",delete_experience,name="delete_experience"),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('register/', register, name='register'),
    path("project/<uuid:project_id>/star/", toggle_star, name="toggle_star"),
    path("project/add-ajax/", create_project_ajax, name="create_project_ajax"),
    path("experience/add-ajax/", create_experience_ajax, name="create_experience_ajax"),
    path("education/add-ajax/", create_education_ajax, name="create_education_ajax"),
]
