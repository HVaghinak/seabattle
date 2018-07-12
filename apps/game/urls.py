from django.urls import path
from . import views

urlpatterns = [
    path('shot/', views.ShotAPIView.as_view()),
]