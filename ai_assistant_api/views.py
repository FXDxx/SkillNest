from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from . import ai_services
# Create your views here.

# Get learning path
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_learning_path(request):
    skills = request.data.get("skills", "").strip()
    if not skills:
        return Response({"message": "error while getting response"}, status=status.HTTP_404_NOT_FOUND)
    result = ai_services.suggest_learning_path(skills)
    return Response({"learning path": result}, status=status.HTTP_200_OK)


# Get project ideas from AI
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_project_idea(request):
    interest = request.data.get("interest", "").strip()
    if not interest:
        return Response({"message": "error while getting response"}, status=status.HTTP_404_NOT_FOUND)
    result = ai_services.suggest_project_ideas(interest)
    return Response({"Project ideas": result}, status=status.HTTP_200_OK)

# Get summarized blog content from AI
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_summarized_blog(request):
    blog_content = request.data.get("blog_content", "").strip()
    if not blog_content:
        return Response({"message": "error while getting response"}, status=status.HTTP_404_NOT_FOUND)
    result = ai_services.summarize_blog(blog_content)
    return Response({"Summarized blog": result}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_resume_feedback(request):
    feedback = request.data.get("feedback", "")
    if not feedback:
        return Response({"message": "error while getting response"}, status=status.HTTP_404_NOT_FOUND)
    result = ai_services.resume_feedback(feedback)
    return Response({"Resume feedback": result}, status=status.HTTP_200_OK)

