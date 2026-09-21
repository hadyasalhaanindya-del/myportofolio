from django.forms import ModelForm, TextInput, Textarea, URLInput
from django import forms

from main.models import Project, Education, Experience

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Project Name",
            "description": "Project Description",
            "tech_stack": "Technology Used",
            "project_url": "Project URL",
            "project_image_url": "Project Image URS",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Describe Your Project",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "title",
            "description",
            "category",
            "status",
            "thumbnail",
        ]

        labels = {
                   "title" : "School or Institution Name",
                   "description" : "Education Description",
                   "category" : "Education Category",
                   "status" : "Education Status",
                   "thumbnail" : "Image URL",
                }

        widgets = {
                    "title": TextInput(
                        attrs={
                            "placeholder": "School or Instituition Name",
                            "maxlength": 255,
                        }
                    ),
                    "description": Textarea(
                        attrs={
                            "placeholder": "Describe Your Education",
                            "rows": 3,
                        }
                    ),

                    "category": forms.Select(
                         choices=[Education.EDUCATION_CHOICES]
                    ),

                    "status": forms.Select(
                         choices=[Education.STATUS_CHOICES]
                    ),
                    
                    "thumbnail": URLInput(
                        attrs={
                            "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                        }
                    ),
                }


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "status",
            "thumbnail",
        ]

        labels = {
                   "title" : "Experience Title",
                   "description" : "Experience Description",
                   "category" : "Experience Category",
                   "status" : "Experience Status",
                   "thumbnail" : "Image URL",
                }

        widgets = {
                    "title": TextInput(
                        attrs={
                            "placeholder": "Experience Title",
                            "maxlength": 255,
                        }
                    ),
                    "description": Textarea(
                        attrs={
                            "placeholder": "Describe Your Experience",
                            "rows": 3,
                        }
                    ),
                    "category": forms.Select(
                         choices=[Experience.EXPERIENCE_CHOICES]
                    ),

                    "status": forms.Select(
                         choices=[Experience.STATUS_CHOICES]
                    ),
                    
                    "thumbnail": URLInput(
                        attrs={
                            "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                        }
                    ),
                }








