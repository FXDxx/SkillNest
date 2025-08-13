from django.urls import path
from . import views
urlpatterns=[
    path('api/get-learning-path', views.get_learning_path, name="get_learning_path"),
    path('api/get-project-ideas', views.get_project_idea, name="get_project_idea"),
    path('api/get-summarized-blogs', views.get_summarized_blog, name="get_summarized_blog"),
    path('api/get-resume-feedback', views.get_resume_feedback, name="get_resume_feedback"),
]