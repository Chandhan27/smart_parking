from django.urls import path
from . import views

urlpatterns = [
    path('', views.find_parking, name='find_parking'),
]
