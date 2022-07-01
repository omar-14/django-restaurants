from rest_framework import serializers
from .models import Restaurant

class RegisterRestaurantSerializers(serializers.Serializer):
  name = serializers.CharField(required = True)
  type = serializers.CharField(required = True)
  address = serializers.CharField(required = True)
  telephone = serializers.CharField(required = True)

class RestaurantSerializer(serializers.Serializer):
  id = serializers.IntegerField(required=True)

class RestaurantSerializers(serializers.ModelSerializer):
  class Meta:
    model = Restaurant()
    fields = ('__all__')

