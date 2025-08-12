from django.shortcuts import render
from .serializers import *
from rest_framework.decorators import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import *
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_blogs(request):
    blog_data = Blog.objects.all()
    blog_data_serializer = BlogSerializer(blog_data, many=True)
    return Response({"Show Blog data": blog_data_serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_new_blog(request):
    user = request.data.get('user')
    try:
        user_id=User.objects.get(id=user)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)
    title=request.data.get("title")
    content=request.data.get("content")
    tags=request.data.get("tags")
    view_count=request.data.get("view_count")
    log_data = Blog.objects.create(
        user=user_id,
        title=title,
        content=content,
        tags=tags,
        view_count=view_count,
    )

    return Response({"message": "New Blog successfully created"}, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_blog(request):
    user = request.user
    user.title=request.data.get("title")
    user.content=request.data.get("content")
    user.tags=request.data.get("tags")
    user.view_count=request.data.get("view_count")
    user.save()
    return Response({"message": "blog user successfully updated"}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_blog(request):
    blog_data = Blog.objects.all()
    if not blog_data:
        return Response({"error":"no blog found"}, status=status.HTTP_404_NOT_FOUND)
    blog_data.delete()

    return Response({"message":"blog deleted successfully"}, status=status.HTTP_200_OK)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def autosave_blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug, author=request.user)
    blog.content = request.data.get('content', blog.content)
    blog.status = 'draft'
    blog.save()
    return Response({"message": "Draft saved!"})

