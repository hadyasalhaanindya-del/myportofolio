from django.shortcuts import render

from main.models import Experience


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