from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_id = models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    bio = models.TextField(max_length=600, null=True)
    profile_photo = models.ImageField(null=True)
    social_link_one = models.URLField(null=True)
    social_link_two = models.URLField(null=True)
    social_link_three = models.URLField(null=True)
