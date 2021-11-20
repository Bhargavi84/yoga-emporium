from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback, name='view_feedback'),
    path('', views.post_detail, name='post_detail'),
]