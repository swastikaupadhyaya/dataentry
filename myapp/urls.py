from django.urls import path 
from . import views

urlpatterns = [
    path("", views.people, name="people"),
    path("new-person/", views.new_person, name="new_person"),
]