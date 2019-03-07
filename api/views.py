from rest_framework import generics
from abcd.models import Todo
from rest_framework import viewsets
from django.shortcuts import render
from .serializers import TodoSerializer

class TodoRud(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

