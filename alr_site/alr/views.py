from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib.auth.models import User, Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import User as alr_user
from .models import BigAudio, Speaker, Language, Review, AudioTrim, Comment, Measurements, Class, Assignment

from . import alr

import datetime
import logging
# testing logging functions
logger = logging.getLogger(__name__)
# Create your views here.

def get_data(self, column):
    query = UserData.objects.get(Username="Stack")
    return getattr(query, column)


# Start of page views
# This is to display a message to the user
active_messages = {'home': '',
                   'settings':'',
                   'signup': '',
                   'evalLogin':'',
                   'viewData': '',
                   'rateData': '',
                   'uploadAudio': '',
                   'trimAudio': '',
                   'userManagement': '',
                   'createEval': '',
                   }


# for alr.hs.umt.edu/viewData/ as url
@login_required(login_url='/home/')
def display_viewData(request):
    if is_user_type(request, ['ADMIN','research_user'], OR=True):
        request = check_message(request, 'viewData')
        return render(request, 'general/ViewData.html')
    else:
        return redirect_home(request)

# for alr.hs.umt.edu/uploadAudio/ as url
@login_required(login_url='/home/')
def display_uploadAudio(request):
    if is_user_type(request, ['ADMIN','research_user'], OR=True):
        request = check_message(request, 'uploadAudio')
        return render(request, 'general/UploadAudio.html')
    else:
        return redirect_home(request)

# @login_required(login_url='/home/')
def display_trimAudio(request):
    return render(request, 'general/TrimAudio.html')

# @login_required(login_url='/home/')
# for alr.hs.umt.edu/rateData/ as url
def display_rateData(request):
    request = check_message(request, 'rateData')
    return render(request, 'rater/RateData.html')

# for alr.hs.umt.edu/userManagement/ as url
@login_required(login_url='/home/')
def display_userManagement(request):
    if is_user_type(request, ['ADMIN','research_user'], OR=True):
        request = check_message(request, 'userManagement')
        return render(request, 'researcher/UserManagement.html')
    else:
        return redirect_home(request)

@login_required(login_url='/home/')
def display_createEval(request):
    if is_user_type(request, ['ADMIN','research_user'], OR=True):
        request = check_message(request, 'createEval')
        return render(request, 'researcher/createEval.html')
    else:
        return redirect_home(request)

@login_required(login_url='/home/')
def display_trimAudio(request):
    request = check_message(request, 'trimAudio')
    return render(request, 'general/TrimAudio.html')

def display_evalLogin(request):
    request = check_message(request, 'evalLogin')
    return render(request, 'rater/RaterLink.html')


# for alr.hs.umt.edu as url
def redirect_home(request):
    return redirect('/home/')

# for alr.hs.umt.edu/home/ as url
def display_home(request):
    request = check_message(request, 'home')
    return render(request, 'public/index.html') ## TODO: change to index.html

# for alr.hs.umt.edu/home/settings as url
@login_required(login_url='/home/')
def display_settings(request):
    request = check_message(request, 'settings')
    return render(request, 'general/AccountSettings.html') ## TODO: change to index.html

# for alr.hs.umt.edu/signUp/ as url
def display_signUp(request):
    request = check_message(request, 'signup')
    return render(request, 'public/SignUp.html')

# for alr.hs.umt.edu/aboutUs/ as url
def display_aboutUs(request):
    return render(request, 'public/AboutUs.html')

# not permanent
def display_taskBar(request):
    return render(request, 'general/TaskBar.html')

# for displaying a meesage to the user
def check_message(request, page):
    if active_messages[page] != '':
        messages.info(request, active_messages[page])
        active_messages[page] = ''
    return request
# end of page views

# start of permission functions # TODO: put in seperate file
def is_user_type(request, input, OR=False, AND=False):
    if type(input) == type(''):
        return request.user.groups.filter(name=type).exists()
    elif type(input) == type([]) and ((OR and not AND) or (not OR and AND)):
        bool = []
        for i in range(len(input)):
            bool.append(request.user.groups.filter(name=input[i]).exists())
        if OR and (True in bool):
            return True
        if AND and (False not in bool):
            return True
        return False


# end of permission functions

# start of ajax calls
# @permission_required(, login_url='/home/')
@csrf_exempt
@login_required(login_url='/home/')
def ajax_getAllAudioTrims(request):
    if is_user_type(request, ['ADMIN','research_user'], OR=True):
        if request.method == 'GET':
            return JsonResponse(alr.GetAllAudioTrim(request), safe=False)
    else:
        return redirect_home(request)

@csrf_exempt
@login_required(login_url='/home/')
def ajax_createEval(request):
    if is_user_type(request, ['ADMIN','research_user'], OR=True):
        if request.method == 'POST':
            active_messages['createEval'] = alr.createEval(request)
            return redirect('researcher/createEval/')


@csrf_exempt
@login_required(login_url='/home/')
def ajax_postRating(request):
    if request.method == 'POST':
        alr.updateRating(request)
        active_messages['rateData'] = 'Your changes have been saved'
        return redirect('/rateData/')
# ajax_postUploadAudio
# @csrf_exempt
# @login_required(login_url='/home/')
# def ajax_postUploadAudio(request):
#     if request.method == 'POST':
#         return JsonResponse(None, safe=False)


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
    #for debugging
    print(request.body)
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
            user_acc = User.objects.create_user(email, email, password, first_name=first, last_name=last) #, groups=Group.)
            user_acc.save()
            # TODO: Make better @Cody Hill-Boss
            group = Group.objects.filter(name='auth_user')
            group1 = Group.objects.filter(name=user_type)
            # print(group)
            # print(group1)
            user_acc.groups.add(group[0])
            user_acc.groups.add(group1[0])
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
        print(e)
        if str(e) == 'UNIQUE constraint failed: auth_user.username':
            active_messages['signup'] = 'That email is already used.'
        else:
            active_messages['signup'] = e
        return redirect('/signUp/')

@csrf_exempt
def ajax_loginEvalUser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        active_messages['evalLogin'] = 'You have successfully logged in'
        return redirect('/eval/RateData/')
    else:
        active_messages['evalLogin'] = 'Your account was not found or Your Pin was incorrect'
        return redirect('/eval/login/')


@csrf_exempt
def ajax_loginUser(request):
    # for debugging: prints to server output
    print(request)
    print(request.body)
    print(request.POST['username'])
    ###############################
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

    print()
    #print(request)
    logout(request)
    active_messages['home'] = 'You are logged out'
    return redirect('/home/')

# this is not even close to being done
@csrf_exempt
def ajax_postUploadAudio(request):


    fileOwner = request.user
    fileFile = request.POST['fileToUpload']
    #fileLength = request.POST['fileLength']
    fileLength = "00:01:03"
    fileSpeakerFirst = request.POST['fileSpeakerFirst']
    fileSpeakerLast = request.POST['fileSpeakerLast']
    fileSpeakerId = None
    # TODO: Add langauge if new language given
    #fileLanguageId = Language.objects.filter(id=request.POST['fileLanguageId']).id
    fileLanguageId = Language.objects.filter(name=request.POST['fileLanguageId'])[0].id
    #print(fileLanguageId)
    try:
        print("********")
        # if speaker in db already
        fileSpeakerId = Speaker.objects.filter(first_name=fileSpeakerFirst, last_name=fileSpeakerLast)[0].id
        #fileSpeakerId = Speaker.objects.filter(first_name='Cody').get_data('User id')
        print(fileSpeakerId)
        print("Here")
        print(Speaker.objects.filter(first_name=fileSpeakerFirst, last_name=fileSpeakerLast)[0].id)
# def get_data(self, column):
#     query = UserData.objects.get(Username="Stack")
#     return getattr(query, column)


    except Exception as e:
        pass
        print("Failed to get speaker")
        print(e)
    else:
        # add speaker to DB
        try:
            pass
        # if new speaker is already a user
            #newSpeaker = Speaker(first_name=fileSpeakerFirst, last_name=fileSpeakerLast, user_id=alr_user.objects.filter(id=User.objects.filter(first_name=fileSpeakerFirst, last_name=fileSpeakerLast)[0].id)[0])
            #newSpeaker.save()
            #fileSpeakerId = newSpeaker.id
        except Exception as e:
            raise
        else:
            pass
            # newSpeaker = Speaker(first_name=fileSpeakerFirst, last_name=fileSpeakerLast, user_id=None)
            # newSpeaker.save()
            # fileSpeakerId = newSpeaker[0].id
    print("---------------")
    print(fileSpeakerId)
    big_audio = BigAudio(sound_file=fileFile, length = fileLength, owner_id=fileOwner, speaker_id=fileSpeakerId, language_id=fileLanguageId)
    big_audio.save()


    # filelength = request.POST['fileLength']



    # create big_audio record
    #big_audio = BigAudio.objects.create_user(sound_file=thisSoundFile) #, groups=Group.)
    # big_audio = BigAudio(sound_file=thisSoundFile, length = thisLength, owner_id=thisOwnerId, language_id=thisLanguageId)
    # big_audio.save()


# end of ajax calls


# start of other functions
@csrf_exempt
def set_password(user, newPass):
    if is_user_type(request, 'auth_user'):
        u = User.objects.get(username=user)
        u.set_password(newPass)
        u.save()
