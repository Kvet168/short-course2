from django.db import models

# Create your models here.

class Teacher (models.Model):
    name = models.CharField(max_length=200)
    sex = models.CharField(max_length=10)
    POB = models.CharField(max_length=200)
    DOB = models.DateField(null=True)
