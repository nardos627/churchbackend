from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password', 'phone_number', 'address', 'role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
