from django.shortcuts import render
from .serializers import *
from rest_framework.decorators import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from . import models

# Create your views here.

@api_view(['GET']) 
def show_profile(request):
    profile_data = Profile.objects.all()
    profile_data_serializer = ProfileSerializers(profile_data, many=True)
    return Response({"User Profile data": profile_data_serializer.data}, status=status.HTTP_200_OK)


@api_view(['PUT']) 
def update_log(request):
    try:
        profile_usr = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return Response({"error":"user not found"}, status=status.HTTP_404_NOT_FOUND)
    profile_usr.date=request.data.get("date")
    profile_usr.topic=request.data.get("topic")
    profile_usr.duration=request.data.get("duration")
    profile_usr.notes=request.data.get("notes")
    profile_usr.save()

    return Response({"message": "User profile successfully updated"}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_log(request):
    profile_data = Profile.objects.all()
    if not profile_data:
        return Response({"error":"no user found"}, status=status.HTTP_404_NOT_FOUND)
    profile_data.delete()

    return Response({"message":"profile deleted successfully"}, status=status.HTTP_200_OK)



