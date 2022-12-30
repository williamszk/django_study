from django.urls import path
from . import views

urlpatterns = [
    path("meetup/", views.index, name="index")
]