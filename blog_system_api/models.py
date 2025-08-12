from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)
    tags = models.CharField(max_length=200, null=True)
    view_count = models.IntegerField()

