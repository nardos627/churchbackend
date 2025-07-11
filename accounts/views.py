from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import RegisterAdminSerializer
from .models import CustomUser

class RegisterAdminView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterAdminSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only superadmin can create

