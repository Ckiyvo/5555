# 2222/project/app/models.py
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class ProjectFile(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='files')
    file_name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default='待处理')
    processed_at = models.DateTimeField(null=True, blank=True)
    file_path = models.CharField(max_length=255)