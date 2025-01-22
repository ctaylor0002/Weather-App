from django.db import models

# Create your models here.

# CRUD tasks (Keep it rough right now but add locked users to this later)

class Task(models.model):
    target_date = models.DateField()
    created_date = models.DateField()
    task_name = models.Charfield(max_length=50)
    task_description = models.Charfield(max_length=200)
    author = models.Charfield(max_length=30)
    # I might want to add info for what the original weather is forecast to be so that I can see if it changed since the creation of the task.