from django.urls import path
from . import views
urlpatterns=[
    path('api/add_log', views.add_new_log, name="add_new_log"),
    path('api/show_log', views.show_logs, name="show_logs"),
    path('api/update_log', views.update_log, name="update_log"),
    path('api/delete_log', views.delete_log, name="delete_log"),
]