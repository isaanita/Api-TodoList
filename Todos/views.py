from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

class ListTodo(generics.ListAPIView):
    queryset = todo.objects.all()
    serializer_class = todoSerializer

class DetailTodo(generics.RetrieveUpdateAPIView):
    queryset = todo.objects.all()
    serializer_class = todoSerializer

class CreateTodo(generics.CreateAPIView):
    queryset = todo.objects.all()
    serializer_class = todoSerializer

class DeleteTodo(generics.DestroyAPIView):
    queryset = todo.objects.all()
    serializer_class = todoSerializer

