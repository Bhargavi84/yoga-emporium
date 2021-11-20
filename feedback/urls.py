from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.feedback, name='view_feedback'),
    path('post_detail/', views.post_detail, name='post_detail'),
]