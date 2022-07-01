from rest_framework import serializers
from .models import User

class RegisterUserSerializers(serializers.Serializer):
  email = serializers.CharField(required = True)
  username = serializers.CharField(required = True)
  password = serializers.CharField(required = True)

class LoginUserSerializers(serializers.Serializer):
  email = serializers.CharField(required = True)
  password = serializers.CharField(required = True)

class ValidateUserSerializers(serializers.Serializer):
  token = serializers.TimeField(required=True)

class UserSerializers(serializers.ModelSerializer):
  class Meta:
    model = User()
    fields = ['email', 'username']