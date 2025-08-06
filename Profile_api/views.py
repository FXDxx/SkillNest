from django.shortcuts import render
from .serializers import *
from rest_framework.decorators import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from . import models

# Create your views here.

@api_view(['GET']) 
@permission_classes([IsAuthenticated])
def show_profile(request):
    profile_data = Profile.objects.all()
    profile_data_serializer = ProfileSerializers(profile_data, many=True)
    return Response({"User Profile data": profile_data_serializer.data}, status=status.HTTP_200_OK)


@api_view(['PUT']) 
@permission_classes([IsAuthenticated])
def update_profile(request):
    try:
        profile_usr = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return Response({"error":"user not found"}, status=status.HTTP_404_NOT_FOUND)
    profile_usr.name=request.data.get("name")
    profile_usr.bio=request.data.get("bio")
    profile_usr.profile_photo=request.data.get("profile_photo")
    profile_usr.social_link_one=request.data.get("social_link_one")
    profile_usr.social_link_two=request.data.get("social_link_two")
    profile_usr.social_link_three=request.data.get("social_link_three")
    
    profile_usr.save()

    return Response({"message": "User profile successfully updated"}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_profile(request):
    profile_data = Profile.objects.all()
    if not profile_data:
        return Response({"error":"no user found"}, status=status.HTTP_404_NOT_FOUND)
    profile_data.delete()

    return Response({"message":"profile deleted successfully"}, status=status.HTTP_200_OK)



