"""Database Comments module"""
from django.db import models


class PlayerEvents(models.Model):
    """Database Comments model"""
    event = models.ForeignKey("Events", on_delete=models.CASCADE)
    player = models.ForeignKey("Players", on_delete=models.CASCADE)
    status = models.ForeignKey("Statuses", on_delete=models.CASCADE)
    