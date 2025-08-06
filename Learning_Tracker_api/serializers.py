from rest_framework import serializers
from .models import *
class LearningLogSerializer(serializers.ModelSerializer):
    class Meta:
        name = LearningLog
        fields = '__all__'

