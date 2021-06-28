"""Database RareUser module"""
from django.db import models
from django.contrib.auth.models import User

class Bosses(models.Model):
    """Database RareUser Model"""
    name = models.CharField(max_length=30)
    boss_image_url = models.CharField(max_length=100)
    dungeon = models.ForeignKey("Dungeons", on_delete=models.CASCADE)
    summary = models.CharField(max_length=300)
    boss_status = models.ForeignKey("BossStatuses", on_delete=models.CASCADE)
    

    
    
    
   