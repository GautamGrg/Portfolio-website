from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    language = models.TextField(default="Python")
    image = models.ImageField()
    # firstskill = models.CharField(max_length=50)

    # Add any additional fields you need
