from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    bio = models.TextField(max_length=600, null=True)
    profile_photo = models.ImageField(null=True)
    social_link_one = models.URLField(null=True)
    social_link_two = models.URLField(null=True)
    social_link_three = models.URLField(null=True)
