from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Exercise
from .serializers import ExerciseSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from rest_framework import mixins, viewsets, permissions
from users.serializers import GetUserSerializer
import pusher
from decouple import config
class ExerciseView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=Exercise.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class=ExerciseSerializer


