from . import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('blogMain/', views.blogMain, name='blogMain'),
    path('blogMain/createBlog/', views.createBlog, name='createBlog'),
    path('blogMain/detail/<int:blog_id>', views.detail, name='detail'),
]
