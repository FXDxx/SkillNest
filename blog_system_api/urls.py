from django.urls import path
from . import views
urlpatterns=[
    path('api/add_blog', views.add_new_blog, name="add_new_blog"),
    path('api/show_blog', views.show_blogs, name="show_blogs"),
    path('api/update_blog', views.update_blog, name="update_blog"),
    path('api/delete_blog', views.delete_blog, name="delete_blog"),
]