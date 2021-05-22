from django.db import models
# Create your models here.

class ToDo(models.Model):
    sno = models.IntegerField()
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=200)
    date_created = models.CharField(max_length=50)

