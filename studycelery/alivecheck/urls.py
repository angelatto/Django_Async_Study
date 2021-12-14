from django.urls import path
from . import views

urlpatterns = [
    path('', views.alive_check),
]

