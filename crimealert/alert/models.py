from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    pass

class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="User")
    content = models.TextField(blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100, blank=False)
    latitude = models.CharField(max_length=20, blank=True, null=False)
    longitude = models.CharField(max_length=20, blank=True, null=False)
    

    def __str__(self):
        return f"New crime alert from {self.user} at {self.location}, {self.longitude}, {self.latitude}"
