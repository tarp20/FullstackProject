from django.shortcuts import render

from core.models import Car
from django.http import JsonResponse
from .serializers import CarSerializer
from rest_framework.viewsets import ModelViewSet,ViewSet


class CarViewSet(ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()