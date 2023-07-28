from django.db import models

# Create your models here.
class React(models.Model):
    student = models.CharField(max_length=30)
    branch = models.CharField(max_length=20)

class Data(models.Model):
    student = models.CharField(max_length=30)
    branch = models.CharField(max_length=20)