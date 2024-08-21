from django.http import Http404
from django.shortcuts import get_object_or_404
from ninja import Router
from django.contrib import auth
import jwt
from authtoken import AuthBearer

from accounts.models import Account
from .schemas import UserProfile, Error, UserProfileEdit
from xxprod.settings import SECRET_KEY


router = Router()

@router.get('/profile', response={200: UserProfile, 401: Error}, auth=AuthBearer())
def profile(request):
    payload = jwt.decode(request.auth, SECRET_KEY, algorithms=['HS256'])
    user_id = payload['user_id']
    user = get_object_or_404(Account, id=user_id)
    return 200, user

@router.patch('/profile', response={201: UserProfile, 401: Error, 409: Error, 400:Error}, auth=AuthBearer())
def profile_patch(request, user: UserProfileEdit):
    payload = jwt.decode(request.auth, SECRET_KEY, algorithms=['HS256'])
    user_id = payload['user_id']
    me = get_object_or_404(Account, id=user_id)
    if user.email:
        me.email = user.email
    me.age = user.age
    me.city = user.city
    me.username = user.username
    me.work_experience = user.work_experience
    me.save()
    return 201, me

@router.get('/profiles/{user_id}', response={200: UserProfile, 401: Error, 404: Error}, auth=AuthBearer())
def profiles(request, user_id:int):
    user = get_object_or_404(Account, id=user_id)
    return 200, user

