from django.urls import path
from . import views
urlpatterns=[
    path('api/profile', views.show_profile),
    path('api/update_profile', views.update_profile),
    path('api/delete_profile', views.delete_profile),
]