import uuid

from django.contrib.auth.models import User
from django.db import models

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
        ('organization', 'Organization'),
    ]

    STATUS_CHOICES = [
            ('on going', 'On Going'),
            ('finished', 'Finished')
        ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='Full-Time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='On Going')
    starred_by = models.ManyToManyField(
        User, related_name="starred_experiences", blank=True
    )
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

    def save(self, *args, **kwargs):
        if self.ended_at is not None:
            self.status = 'finished'
        else:
            self.status = 'on going'
        super().save(*args, **kwargs)

class Education(models.Model):
    EDUCATION_CHOICES = [
        ('school', 'School'),
        ('university', 'University')
    ]

    STATUS_CHOICES = [
        ('on going', 'On Going'),
        ('finished', 'Finished')
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EDUCATION_CHOICES, default='School')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='On Going')
    starred_by = models.ManyToManyField(
        User, related_name="starred_educations", blank=True
    )
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

    def save(self, *args, **kwargs):
        if self.ended_at is not None:
            self.status = 'finished'
        else:
            self.status = 'on going'
        super().save(*args, **kwargs)

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255)
    project_url = models.URLField(blank=True)
    project_image_url = models.URLField(blank=True, max_length=500)

    def __str__(self):
        return self.title

    starred_by = models.ManyToManyField(
        User, related_name="starred_projects", blank=True
    )

    


