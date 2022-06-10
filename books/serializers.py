from dataclasses import fields
from rest_framework import serializers
from books.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'