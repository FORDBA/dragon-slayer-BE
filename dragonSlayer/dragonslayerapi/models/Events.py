"""Database Comments module"""
from django.db import models
from django.contrib.auth.models import User


class Events(models.Model):
    """Database Comments model"""
    date = models.DateField()
    name = models.CharField(max_length=50)
    player = models.ForeignKey("Players", on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
