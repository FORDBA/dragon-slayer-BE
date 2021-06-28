"""Database Comments module"""
from django.db import models
from django.contrib.auth.models import User

class BossComments(models.Model):
    """Database Comments model"""
    boss = models.ForeignKey("Bosses", on_delete=models.CASCADE)
    player = models.ForeignKey("Players", on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    