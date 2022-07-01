from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterRestaurantSerializers, RestaurantSerializers, RestaurantSerializer
from .models import Restaurant
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class RestaurantsRegister(APIView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        data = RegisterRestaurantSerializers(data=request.data)

        if data.is_valid():
            name = request.data['name']
            restaurant = list(Restaurant.objects.filter(name=name).values())
            # print(restaurant, '\n\n\n')
            if len(restaurant) > 0:
                return Response(data={
                    'message': 'Restaurant was already registered',
                })
            else:
                restaurant = Restaurant.objects.register_restaurant(data=data.validated_data)
                return Response(data={
                    'message': 'Restaurant was registered',
                    'data': RestaurantSerializers(restaurant).data
                })
        else:
            return Response(data={
                'message': 'Bad Request',
                'error': data.errors
            })

class RestaurantDelete(APIView):
    def delete(self, request, id):
        data = RestaurantSerializer(data={'id': id})

        if data.is_valid():
            restaurant = list(Restaurant.objects.filter(id=id).values())
            if len(restaurant) > 0:
                Restaurant.objects.filter(id=id).delete()
                return Response({
                    'message': 'Restaurant deleted',
                    'data': True
                })
            else:
                return Response({
                    'message': 'Restaurant not found',
                })
        else:
            return Response(data={
                'message': 'Bad Request',
                'error': data.errors
            })

class RestaurantList(APIView):
    def get(self, request):
        restaurant = list(Restaurant.objects.filter().values())
        if len(restaurant) > 0:
            restaurant_serial = RestaurantSerializers(restaurant, many=True).data
            return Response(data={
                'message': 'Restaurants',
                'data': restaurant_serial
            })
        else:
            return Response(data={
                'message': 'Restaurants not found',
            })

class RestaurantUpdate(APIView):
    def put(self, request, id):
        data = RestaurantSerializer(data={'id': id})
        data_restauratnt = RegisterRestaurantSerializers(data=request.data)

        if data.is_valid() and data_restauratnt.is_valid():
            index = dict(data.validated_data)
            restaurants = list(Restaurant.objects.filter(id=index['id']).values())
            if len(restaurants) > 0:
                new_data = dict(data_restauratnt.validated_data)
                restaurant = Restaurant.objects.filter(id=id).values().first()
                restaurant['name'] = new_data['name']
                restaurant['type'] = new_data['name']
                restaurant['address'] = new_data['address']
                restaurant['telephone'] = new_data['telephone']
                restaurant.save()
                return Response(data={
                    'message': 'Restaurant was updated',
                    'data': RestaurantSerializers(restaurant).data
                })
            else:
                return Response(data={
                    'message': 'Restaurant not found',
                })
        else:
            errors = []
            if not data.is_valid():
                errors.append(data.errors)

            if not data_restauratnt.is_valid():
                errors.append(data_restauratnt.errors)
            
            return Response(data={
                'message': 'Bad Request',
                'error': errors
            })