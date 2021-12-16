from django.urls import path
from . import views


urlpatterns = [
    path('',views.pika_test),
]