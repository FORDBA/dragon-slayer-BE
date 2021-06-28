"""Database Comments module"""
from django.db import models
from django.contrib.auth.models import User

class UserProfessions(models.Model):
    """Database Comments model"""
    profession = models.ForeignKey("Professions", on_delete=models.CASCADE)
    player = models.ForeignKey("Players", on_delete=models.CASCADE)
    
    