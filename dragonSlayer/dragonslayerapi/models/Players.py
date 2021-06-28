"""Database RareUser module"""
from django.db import models
from django.contrib.auth.models import User

class Players(models.Model):
    """Database RareUser Model"""
    bio = models.CharField(max_length=300)
    profile_image_url = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    role = models.ForeignKey("Roles", on_delete=models.CASCADE)
    rank = models.ForeignKey("Ranks", on_delete=models.CASCADE)
    player_class = models.ForeignKey("PlayerClasses", on_delete=models.CASCADE)
    race = models.ForeignKey("Races", on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    
    @property
    def username(self):
        return f"{self.user.username}"

    @property
    def is_staff(self):
        return self.user.is_staff
        
    @property
    def email(self):
        return f"{self.user.email}"

    
    
   