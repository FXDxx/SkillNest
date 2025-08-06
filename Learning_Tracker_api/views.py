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
def add_new_log(request, usr_id):
    user_id=usr_id
    date=request.data.get("date")
    topic=request.data.get("topic")
    duration=request.data.get("duration")
    notes=request.data.get("notes")
    

    log_data = LearningLog.objects.create(
        user_id=user_id,
        date=date,
        topic=topic,
        duration=duration,
        notes=notes,
    )

    return Response({"message": "New log successfully created"}, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_log(request, usr_id):
    try:
        log_usr = LearningLog.objects.get(id=usr_id)
    except LearningLog.DoesNotExist:
        return Response({"error":"log not found"}, status=status.HTTP_404_NOT_FOUND)
    log_usr.date=request.data.get("date")
    log_usr.topic=request.data.get("topic")
    log_usr.duration=request.data.get("duration")
    log_usr.notes=request.data.get("notes")
    log_usr.save()

    return Response({"message": "log user successfully updated"}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_log(request):
    log_data = LearningLog.objects.all()
    if not log_data:
        return Response({"error":"no log found"}, status=status.HTTP_404_NOT_FOUND)
    log_data.delete()

    return Response({"message":"log deleted successfully"}, status=status.HTTP_200_OK)



