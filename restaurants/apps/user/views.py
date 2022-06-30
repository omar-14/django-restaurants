import email
from urllib.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from .authenticate import *
from .serializers import UserSerializers
from .models import User
from .serializers import RegisterUserSerializers

class Users(APIView):

  def get(self, request):
    return Response(data = { 'message': 'buebos' })

  def post(self, request):
    data = RegisterUserSerializers(data = request.data)

    if data.is_valid():
      user = User.objects.register_user(data = data.validated_data)

      token = create_token(email= user.email, password= user.password)

      return Response(data = { 'message': UserSerializers(user).data, 'token': token })
    else:
      return Response(data = { 'message': False, 'error': data.errors })

class GetUser(APIView):

  def get(self, request):
    user = User.objects.filter(email= 'omarramos@gmail.com')
    userSeria = UserSerializers(user, many= True).data
    return Response(data = { 'message': userSeria })

  # def post(self, request):
  #   data = RegisterUserSerializers(data = request.data)

  #   if data.is_valid():
  #     user = User.objects.register_user(data = data.validated_data)

  #     token = create_token(email= user.email, password= user.password)

  #     return Response(data = { 'message': UserSerializers(user).data, 'token': token })
  #   else:
  #     return Response(data = { 'message': False, 'error': data.errors })