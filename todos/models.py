#todos/model.py
from django.db import models

class Todo(models.Model):
    title = models.CharField("Your title",max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    