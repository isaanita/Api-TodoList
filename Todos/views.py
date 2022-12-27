from django.shortcuts import render
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
from rest_framework import generics, filters
=======
from rest_framework import generics, filters, permissions
>>>>>>> 9fd54b2b5cf14415358bfa51751390df7044cf30
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend

class ListTodo(generics.ListAPIView):
    queryset = todo.objects.all()
    serializer_class = todoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'description', 'date', 'completed']
    permission_classes = [permissions.IsAuthenticated]

class DetailTodo(generics.RetrieveUpdateAPIView):
    queryset = todo.objects.all()
    serializer_class = todoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'description', 'date', 'completed']
    permission_classes = [permissions.IsAuthenticated]

class CreateTodo(generics.CreateAPIView):
    queryset = todo.objects.all()
    serializer_class = todoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'description', 'date', 'completed']
    permission_classes = [permissions.IsAuthenticated]

class DeleteTodo(generics.DestroyAPIView):
    queryset = todo.objects.all()
    serializer_class = todoSerializer
    permission_classes = [permissions.IsAuthenticated]

@login_required
def dashboard(request): 
    return render(request, 'registration/dashboard.html', {'section': 'dashboard'})
