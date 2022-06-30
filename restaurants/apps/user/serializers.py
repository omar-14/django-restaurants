from rest_framework import serializers
from .models import User

class RegisterUserSerializers(serializers.Serializer):
  email = serializers.CharField(required = True)
  user_name = serializers.CharField(required = True)
  password = serializers.CharField(required = True)

class UserSerializers(serializers.ModelSerializer):
  class Meta:
    model = User()
    fields = ['email', 'user_name']