from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
# from .models import # TODO: db tables
from . import alr.py

# TODO: This is would allow users to Publish a post for example, might be useful
# from myapp.models import BlogPost
#
# def create_Permissions():
#     content_type = ContentType.objects.get_for_model(BlogPost)
#     permission = Permission.objects.create(
#         codename='can_publish',
#         name='Can Publish Posts',
#         content_type=content_type,
#     )

@csrf_exempt
def ajax_loginUser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/home/')
    else:
        return redirect('/home/')

@csrf_exempt
def ajax_logoutUser(request):
    logout(request)
    return redirect('/home/')

def auth_user(user, password):
    user = authenticate(username=user, password=password)
    if user is not None:
        pass
        # A backend authenticated the credentials
    else:
        pass
        # No backend authenticated the credentials

def set_password(user, newPass):
    u = User.objects.get(username=user)
    u.set_password(newPass)
    u.save()

def create_user(first, last, email, password):
    u = User.objects.create_user(first, email, password, last_name=last)
    u.save()
