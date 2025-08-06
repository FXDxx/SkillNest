from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import LogoutUserSerializer

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LogoutUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail", "logout successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTPS)