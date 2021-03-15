from . import views
from django.urls import path
from django.contrib import admin

app_name = "blogapp"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('blogMain/', views.blogMain, name='blogMain'),
    path('blogMain/createBlog/', views.createBlog, name='createBlog'),
    path('blogMain/detail/<int:blog_id>', views.detail, name='detail'),
]
