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
from alr.models import User as alr_user
from . import alr

# Create your views here.

# Start of page views
# This is to display a message to the user
active_messages = {'viewData': '', 'home': '', 'signup': '' }

@login_required(login_url='/home/')
def display_viewData(request):
    return render(request, 'general/ViewData.html')

def redirect_home(request):
    return redirect('/home/')

def display_home(request):
    if active_messages['home'] != '':
        messages.info(request, active_messages['home'])
        active_messages['home'] = ''
    return render(request, 'public/index.html') ## TODO: change to index.html

def display_taskBar(request):
    return render(request, 'general/TaskBar.html')


def display_aboutUs(request):
    return render(request, 'public/AboutUs.html')

def display_signUp(request):
    if active_messages['signup'] != '':
        messages.info(request, active_messages['signup'])
        active_messages['signup'] = ''
    return render(request, 'public/SignUp.html')

# end of page views

# start of ajax calls
@csrf_exempt
@login_required(login_url='/home/')
def ajax_getAllAudioTrims(request):
    if request.method == 'GET':
        return JsonResponse(alr.GetAllAudioTrim(), safe=False)

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
def ajax_createUser(request):
    # try authenticating the user
    user = authenticate(request=None, username=request.POST['email'], password=request.POST['password'])

    # if None then user DNE
    try:
        if user is None:
            first = request.POST['firstname']
            last = request.POST['lastname']
            email = request.POST['email']
            password = request.POST['password']
            user_type = request.POST['user_type']

            # create django user
            user_acc = User.objects.create_user(email, email, password, first_name=first, last_name=last)
            user_acc.save()
            # create alr user
            u = alr_user(id=user_acc, type=user_type)
            u.save()

            user = authenticate(request, username=email, password=password)
            # login new user
            if user is not None:
                login(request, user)
                active_messages['home'] = 'You have successfully logged in'
                return redirect('/home/')
            else:
                active_messages['signup'] = 'Your account was not created for some reason'
                return redirect('/signUp/')
        else:
            active_messages['signup'] = 'That email is already used.'
            return redirect('/signUp/')
    except Exception as e:
        if str(e) == 'UNIQUE constraint failed: auth_user.username':
            active_messages['signup'] = 'That email is already used.'
        else:
            active_messages['signup'] = e
        return redirect('/signUp/')


@csrf_exempt
def ajax_loginUser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        active_messages['home'] = 'You have successfully logged in'
        return redirect('/home/')
    else:
        active_messages['home'] = 'Your account was not found or Your password was incorrect'
        return redirect('/home/')

@csrf_exempt
def ajax_logoutUser(request):
    logout(request)
    active_messages['home'] = 'You are logged out'
    return redirect('/home/')

# end of ajax calls

# start of other functions
# might not need
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
