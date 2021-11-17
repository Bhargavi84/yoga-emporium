from django.urls import path
from . import views


urlpatterns = [
    path('post_detail/<str:slug>/', views.post_detail, name='post_detail'),
]