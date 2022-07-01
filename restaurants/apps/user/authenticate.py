import jwt
from datetime import datetime
from datetime import timedelta
from rest_framework import authentication

def create_token(email, password):
    return jwt.encode({'email': email,
        'password': password, 
        'exp': datetime.now() + timedelta(minutes=15)},
        'secret',
        algorithm='HS256')

def validate_token(token):
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        return payload
    except:
        return None

class TokenAuthentication(authentication.BasicAuthentication):
    def authenticate(self, request):
        pass