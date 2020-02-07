from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from alr.models import AudioTrim
from . import alr

# Create your views here.

# Start of page views

active_messages = {'viewData': '', 'home': '', }

@login_required(login_url='/home/')
def display_viewData(request):
    return render(request, 'general/ViewData.html')

def display_home(request):
    print(active_messages['home'])
    if active_messages['home'] != '':
        messages.info(request, active_messages['home'])
        active_messages['home'] = ''
    return render(request, 'public/index.html') ## TODO: change to index.html

def display_aboutUs(request):
    return render(request, 'public/AboutUs.html')

def display_signUp(request):
    return render(request, 'public/SignUp.html')

# end of page views

# start of ajax calls
@csrf_exempt
@login_required(login_url='/home/')
def ajax_getAllAudioTrims(request):
    if request.method == 'GET':
        return JsonResponse(alr.GetAllAudioTrim(), safe=False)

# @csrf_exempt
# @login_required(login_url='/home/')
# def ajax_getAllAudioTrims(request):
#     if request.user.is_authenticated:
#         pass
#     else:
#         pass
#
#     if request.method == 'GET':
#         return JsonResponse(alr.GetAllAudioTrim(request.user), safe=False)


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

#
# @login_required(login_url='/home/')
# def post_delete(request, id=None):
#     ...
#


@csrf_exempt
def ajax_createUser(first, last, email, password):
    # try authenticating the user
    user = authenticate(request, username=email, password=password)
    # if None then user DNE
    if user is None:
        # create user
        u = User.objects.create_user(first, email, password, last_name=last)
        u.save()
        # authenticate user
        user = authenticate(request, username=email, password=password)
        # log this new user in
        login(request, user)
        # messages.info(request, 'Some Message')
        return redirect('/home/')
    else:
        # messages.info(request, 'Some Message')
        return redirect('/SignUp/')

@csrf_exempt
def ajax_loginUser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        active_messages['home'] = 'You have successfully logged in'
        return redirect('/home/')
        # return display_home(request)
    else:
        active_messages['home'] = 'Your account was not found or Your password was incorrect'
        return redirect('/home/')

@csrf_exempt
def ajax_logoutUser(request):
    logout(request)
    return redirect('/home/')

# end of ajax calls

# start of other functions
def auth_user(username, password):
    user = authenticate(username=username, password=password)
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

# end of other functions
