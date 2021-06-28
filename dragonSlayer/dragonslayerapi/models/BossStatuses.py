"""Database Tag module"""
from django.db import models

class BossStatuses(models.Model):
    """Database Tag model"""
    name = models.CharField(max_length=50)