from django.db import models
from Profile_api.models import *
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class LearningLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    topic = models.CharField(max_length=50, null=True)
    duration = models.PositiveIntegerField()
    notes = models.TextField()


