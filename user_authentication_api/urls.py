from django.urls import path
from .views import LogoutAPIView
urlpatterns = [
    path("jwt/logout/", LogoutAPIView.as_view(), name="jwt-logout"),
]