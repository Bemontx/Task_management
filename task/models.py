from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    deadline = models.DateField()
    status_choices = [
        ('P', 'Pendiente'),
        ('E', 'En progreso'),
        ('C', 'Completada'),
    ]
    status = models.CharField(max_length=1, choices=status_choices, default='P')

    def __str__(self):
        return self.title
