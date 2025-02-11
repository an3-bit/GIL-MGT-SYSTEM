
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import (
    TitleTransferTypes, TitleProcess, Client, 
    Surveyor, Payment, TitleDocument, User
)

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

# ... keep existing code (other serializer classes)
