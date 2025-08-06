from django.shortcuts import render
from .serializers import *

from rest_framework.decorators import *
#from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import *
from rest_framework.permissions import IsAuthenticated
# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_logs(request):
    log_data = LearningLog.objects.all()
    log_data_serializer = LearningLogSerializer(log_data, many=True)
    return Response({"New log data": log_data_serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_new_log(request):
    date=request.data.get("date")
    topic=request.data.get("topic")
    duration=request.data.get("duration")
    notes=request.data.get("notes")
    

    log_data = LearningLog.objects.create(
        user=request.user,
        date=date,
        topic=topic,
        duration=duration,
        notes=notes,
    )

    return Response({"message": "New log successfully created"}, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_log(request):
    user = request.user
    user.date=request.data.get("date")
    user.topic=request.data.get("topic")
    user.duration=request.data.get("duration")
    user.notes=request.data.get("notes")
    user.save()

    return Response({"message": "log user successfully updated"}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_log(request):
    log_data = LearningLog.objects.all()
    if not log_data:
        return Response({"error":"no log found"}, status=status.HTTP_404_NOT_FOUND)
    log_data.delete()

    return Response({"message":"log deleted successfully"}, status=status.HTTP_200_OK)



