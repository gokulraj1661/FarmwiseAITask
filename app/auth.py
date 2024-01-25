from App.models import users
from flask_jwt import JWT

def authenticate(username, password):
    user = next((user for user in users if user.username == username and user.password == password), None)
    if user:
        return user

def identity(payload):
    user_id = payload['identity']
    return next((user for user in users if user.username == user_id), None)

jwt = JWT(authenticate, identity)
