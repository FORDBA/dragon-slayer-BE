"""Database Comments module"""
from django.db import models


class Treasures(models.Model):
    """Database Comments model"""
    boss = models.ForeignKey("Bosses", on_delete=models.CASCADE)
    player = models.ForeignKey("Players", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    reason = models.CharField(max_length=300)