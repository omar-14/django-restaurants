import email
from rest_framework.views import APIView
from rest_framework.response import Response
from .authenticate import *
from .serializers import UserSerializers
from .models import User
from .serializers import RegisterUserSerializers, ValidateUserSerializers, LoginUserSerializers


class Users(APIView):

    def post(self, request):
        data = RegisterUserSerializers(data=request.data)

        if data.is_valid():
            email = request.data['email']
            users = list(User.objects.filter(email=email).values())
            if len(users) <= 0:
                user = User.objects.register_user(data=data.validated_data)
                return Response(data={
                    'message': 'User was registered',
                    'data': UserSerializers(user).data
                })
            else:
                return Response(data={
                    'message': 'User was already registered'
                })
        else:
            return Response(data={
                'message': 'Bad request',
                'error': data.errors
            })

class LoginUser(APIView):
    def post(self, request):
        data = LoginUserSerializers(data=request.data)

        if data.is_valid():
            data_serial = dict(data.validated_data)
            email = data_serial['email']
            password = data_serial['password']
            users = list(User.objects.filter(email=email, password=password))
            if len(users) > 0:
                user = User.objects.filter(email=email, password=password).values().first()
                
                token = create_token(email=user['email'], password=user['password'])
                return Response(data={
                        'message': 'Found user',
                        'data': UserSerializers(user).data,
                        'token': token
                    })
            else:
                return Response(data={
                    'message': 'User not found'
                })
        else:
            return Response(data={
                    'message': 'Bad request',
                    'errors': data.errors
                })


class GetUser(APIView):

    def get(self, request, email):
        user = User.objects.filter(email=email)
        user_serial = UserSerializers(user, many=True).data
        return Response(data={'message': user_serial})

    def post(self, request):
        data = ValidateUserSerializers(data=request.data)
        if data.is_valid():
            token = dict(data.validated_data)
            token = validate_token(token=token['token'])

            return Response(data={
                'message': UserSerializers(token).data,
                'token': token
            })
        else:
            return Response(data={
                'message': False,
                'error': data.errors
            })
