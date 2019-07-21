from django.urls import path

from .views import plant_details

urlpatterns = [
    path("plant/<int:plant_id>", plant_details, name="plant_details"),
]
