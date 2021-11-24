from django.db import models

# Create your models here.
class Tasks(models.Model):
    userid = models.CharField(max_length = 20)
    task = models.CharField(max_length = 100)
