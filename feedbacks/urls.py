from django.urls import path
from . import views


urlpatterns = [
    path('', views.feedbacks, name='feedbacks'),
    path('<slug>/', views.comments_details, name='comments_details'),
]