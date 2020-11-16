
from django.urls import path
from .views import all_cars

urlpatterns = [
    path('cars/',all_cars,)
]
