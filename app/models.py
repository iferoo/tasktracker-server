from django.db import models

# Create your models here.

class Task(models.Model):
    text = models.CharField(max_length=70, null=True)
    day = models.CharField(max_length=70, null=True)
    reminder = models.BooleanField(null=True)
