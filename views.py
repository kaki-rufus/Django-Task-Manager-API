from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset =  Todo.objects.all()
