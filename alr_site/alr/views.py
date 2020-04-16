# **************************************************************************** #
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse, FileResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import os

from .models import User as alr_user
from .models import BigAudio, Speaker, Language, Review, AudioTrim, Comment, Measurements, Class, Assignment
#> from django.contrib.auth.models import User

from . import alr

import datetime
# **************************************************************************** #

#import logging
# testing logging functions
#logger = logging.getLogger(__name__)
# Create your views here.

# from nate, will remove when I remmeber why I wanted it
# def get_data(self, column):
#     query = UserData.objects.get(Username="Stack")
#     return getattr(query, column)


#                           Global variables
# **************************************************************************** #
# This is to display a message to the user
active_messages = {'home': '',
                   'settings':'',
                   'signup': '',
                   'evalLogin':'',
                   'viewAudio': '',
                   'rateAudio': '',
                   'uploadAudio': '',
                   'trimAudio': '',
                   'shareAudio': '',
                   'createEval': '',
                   }

# **************************************************************************** #

#                           Start of page views
# **************************************************************************** #

# for alr.hs.umt.edu/viewAudio/ as URL
# If you are not logged in, and not an admin or researcher, it will redirect to login_url
# Called whenever the URL is accessed
@login_required(login_url='/home/')
def display_viewAudio(request):
    if is_user_type(request, ['ADMIN','research_user'], OR=True):
        request = check_message(request, 'viewAudio')
        return render(request, 'general/ViewAudio.html')
    else:
        return redirect_home(request)

# for alr.hs.umt.edu/uploadAudio/ as URL
# If you are not logged in, and not an admin or researcher, it will redirect to home page
# Called whenever the URL is accessed
@login_required(login_url='/home/')
def display_uploadAudio(request):
    if is_user_type(request, ['ADMIN','research_user', 'student_user'], OR=True):
        request = check_message(request, 'uploadAudio')
        return render(request, 'general/UploadAudio.html')
    else:
        return redirect_home(request)

# for alr.hs.umt.edu/RateAudio/ as url
@login_required(login_url='/home/')
def display_rateAudio(request):
    if is_user_type(request, ['ADMIN','eval_user'], OR=True):
        request = check_message(request, 'rateAudio')
        return render(request, 'rater/RateAudio.html')
    else:
        return redirect_home(request)

# for alr.hs.umt.edu/ShareAudio/ as url
@login_required(login_url='/home/')
def display_shareAudio(request):
    #TODO Add evaluators to permissions?
    if is_user_type(request, ['ADMIN','research_user'], OR=True):
        request = check_message(request, 'shareAudio')
        return render(request, 'researcher/ShareAudio.html')
    else:
        return redirect_home(request)

#For researchers to create accounts for evaluators
@login_required(login_url='/home/')
def display_createEval(request):
    if is_user_type(request, ['ADMIN','research_user'], OR=True):
        request = check_message(request, 'createEval')
        return render(request, 'researcher/createEval.html')
    else:
        return redirect_home(request)

@login_required(login_url='/home/')
def display_trimAudio(request):
    # TODO: remove active set
    # active_messages["trimAudio"] = str(1) + ' ' + str('a.wav')
    messages.success(request, active_messages["trimAudio"])
    # try:
    #     if type(parseInt(active_messages["trimAudio"])) == type(426):
    #         messages.success(request, parseInt(active_messages["trimAudio"]))
    #         active_messages["trimAudio"] = ''
    # except:
    #     print(active_messages["trimAudio"])
    # else:
    #     request = check_message(request, 'trimAudio')


    return render(request, 'general/TrimAudio.html')

# A simplified login view for evaluator accounts made by researchers
def display_evalLogin(request):
    request = check_message(request, 'evalLogin')
    return render(request, 'rater/RaterLink.html')

# TODO: rearange functions
# **************************************************************************** #

# for alr.hs.umt.edu as url
def redirect_home(request):
    return redirect('/home/')

# for alr.hs.umt.edu/home/ as url
def display_home(request):
    request = check_message(request, 'home')
    return render(request, 'public/index.html')

# for alr.hs.umt.edu/home/settings as url
@login_required(login_url='/home/')
def display_settings(request):
    request = check_message(request, 'settings')
    return render(request, 'general/AccountSettings.html')

# for alr.hs.umt.edu/signUp/ as url
# log_out required?
def display_signUp(request):
    request = check_message(request, 'signup')
    return render(request, 'public/SignUp.html')

# for alr.hs.umt.edu/aboutUs/ as url
def display_aboutUs(request):
    return render(request, 'public/AboutUs.html')

# not permanent
# TODO remove when no longer used
def display_taskBar(request):
    return render(request, 'general/TaskBar.html')
def display_test1(request):
    return render(request, 'tempViewData.html')
def display_test2(request):
    return render(request, 'tempRateData.html')

# for displaying a meesage to the user
# Attaches messages to the request from the active_messages dict
def check_message(request, page):
    if active_messages[page] != '':
        messages.info(request, active_messages[page])
        active_messages[page] = ''
    return request

#                           end of page views
# **************************************************************************** #

# start of permission functions # TODO: put in seperate file?
# some accounts are have multiple roles.  OR and AND handle those cases
# OR and AND are flags, For example, set OR to true if you want the function to return true if
# the request comes from a user who has any of the roles given in input
# The OR and AND flags cannot be both true  or it returns false

# input can be a string or and array of strings (e.g. "ADMIN" or ["ADMIN", "researcher_user"])
def is_user_type(request, input, OR=False, AND=False):
    if type(input) == type(str()):
        return request.user.groups.filter(name=type).exists()
    elif type(input) == type(list()) and ((OR and not AND) or (not OR and AND)):
        bool = []
        for i in range(len(input)):
            bool.append(request.user.groups.filter(name=input[i]).exists())
        if OR and (True in bool):
            return True
        if AND and (False not in bool):
            return True
        return False
    return False

#                       end of permission functions
# **************************************************************************** #

#                           start of ajax calls
# **************************************************************************** #

@csrf_exempt
@login_required(login_url='/home/')
def ajax_getAllAudioTrims(request):
    if is_user_type(request, ['ADMIN','research_user'], OR=True):
        if request.method == 'GET':
            if is_user_type(request, ['ADMIN'], OR=True):
                return JsonResponse(alr.getAllAudioTrim(request, True), safe=False)
            return JsonResponse(alr.getAllAudioTrim(request), safe=False)

    else:
        return redirect_home(request)

@csrf_exempt
@login_required(login_url='/home/')
def ajax_getAllLanguages(request):
    if is_user_type(request, ['ADMIN','research_user'], OR=True):
        if request.method == 'GET':
            return JsonResponse(alr.getAllLanguages(request), safe=False)
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
def ajax_getAudioFileById(request):
    if is_user_type(request, ['ADMIN','auth_user'], OR=True):
        if request.method == 'GET':
            Audio = BigAudio.objects.get(id=request.GET['id'])
            return HttpResponse(Audio.sound_file.url)
    else:
        return redirect_home(request)

@csrf_exempt
@login_required(login_url='/home/')
def ajax_postRating(request):
    if is_user_type(request, ['ADMIN','eval_user'], OR=True):
        if request.method == 'POST':
            # alr.updateRating(request)
            active_messages['rateAudio'] = 'Your changes have been saved'
            return redirect('/rateAudio/')

# legacy? new ajax_postUploadAudio is below
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
    # print(request.body)
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
        return redirect('/eval/RateAudio/')
    else:
        active_messages['evalLogin'] = 'Your account was not found or Your Pin was incorrect'
        return redirect('/eval/login/')


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

# For uploading files (found in uploadAudio page)
@csrf_exempt
@login_required(login_url='/home/')
def ajax_postUploadAudio(request):
    print("You have reached ajax_post uploaded audio in views.py")
    if is_user_type(request, ['ADMIN','research_user', 'student_user'], OR=True):
        if request.method == 'POST':
            #compare to request.user  #nate TODO change request.files in upload recording to request.blob
            fileOwner = alr_user.objects.get(id=User.objects.get(email=str(request.user)))
            fileFile = request.FILES['fileToUpload']
            # print(fileFile)
            import wave as wv
            import math
            f = wv.open(fileFile)
            secs = f.getnframes() / f.getframerate()
            secs = math.ceil(secs)
            l = '0' + str(datetime.timedelta(seconds=secs))
            # print(l)

            # print(wv.open(fileFile).getnframes())

            # print(fileFile)
            # print(fileFile.duration)
            fileLength = "00:01:03"
            fileSpeakerFirst = request.POST['fileSpeakerFirst']
            fileSpeakerLast = request.POST['fileSpeakerLast']
            fileSpeakerId = None
            # TODO: Add langauge if new language given
            fileLanguageId = Language.objects.get(name=request.POST['fileLanguageId'])

            # if speaker in db already
            try:
                fileSpeakerId = Speaker.objects.get(first_name=fileSpeakerFirst, last_name=fileSpeakerLast)
            except Exception as e:
                # TODO: Finish This
                # add speaker to DB
                try:
                    # if new speaker is already a user
                    newSpeaker = Speaker(first_name=fileSpeakerFirst, last_name=fileSpeakerLast, user_id=alr_user.objects.get(id=User.objects.get(first_name=fileSpeakerFirst, last_name=fileSpeakerLast)))
                    newSpeaker.save()
                    fileSpeakerId = newSpeaker
                except Exception as e:
                    newSpeaker = Speaker(first_name=fileSpeakerFirst, last_name=fileSpeakerLast, user_id=None)
                    newSpeaker.save()
                    fileSpeakerId = newSpeaker
            if not os.path.isfile(settings.MEDIA_ROOT + 'user_' + str(request.user.id) + '_big/' + str(fileFile)):
                big_audio = BigAudio(sound_file=fileFile, length = fileLength, owner_id=fileOwner, speaker_id=fileSpeakerId, language_id=fileLanguageId)
                big_audio.save()
            else:
                active_messages["uploadAudio"] = 'File with that name already exists'
                return redirect('/uploadAudio/')
            active_messages["trimAudio"] = 'File succesfully uploaded'
            return redirect('/trimAudio/')
        else:
            redirect('/uploadAudio/')
    else:
        redirect('/uploadAudio/')


def ajax_postTrimAudio(request):
    pass

#/ajax/postRecordedAudio
#*******************************************   FOr uploading recordings (same as uploading files) ************************

@csrf_exempt
@login_required(login_url='/home/')
def ajax_postRecordedAudio(request):
    print("You have reached ajax_post recoreded audio in views.py")
    if is_user_type(request, ['ADMIN','research_user'], OR=True):
        if request.method == 'POST':
            fileOwner = alr_user.objects.get(id=User.objects.get(email=str(request.user)))

            fileFile = request.FILES['recordingToUpload']
            print(fileFile)
            import wave as wv
            import math
            f = wv.open(fileFile)
            secs = f.getnframes() / f.getframerate()
            secs = math.ceil(secs)
            l = '0' + str(datetime.timedelta(seconds=secs))
            # print(l)


            # print(wv.open(fileFile).getnframes())

            # print(fileFile)
            # print(fileFile.duration)
            fileLength = "00:01:03"
            fileSpeakerFirst = request.POST['fileSpeakerFirst']
            fileSpeakerLast = request.POST['fileSpeakerLast']
            fileSpeakerId = None
            # TODO: Add langauge if new language given
            fileLanguageId = Language.objects.get(name=request.POST['fileLanguageId'])

            try:
                # if speaker in db already
                fileSpeakerId = Speaker.objects.get(first_name=fileSpeakerFirst, last_name=fileSpeakerLast)
            except Exception as e:
                pass
                print("Failed to get speaker")
                print(e)
            else:
                # TODO: Finish This
                # add speaker to DB
                try:
                    pass
                    # if new speaker is already a user
                    # newSpeaker = Speaker(first_name=fileSpeakerFirst, last_name=fileSpeakerLast, user_id=alr_user.objects.get(id=User.objects.get(first_name=fileSpeakerFirst, last_name=fileSpeakerLast)))
                    # newSpeaker.save()
                    # fileSpeakerId = newSpeaker
                except Exception as e:
                    raise
                else:
                    pass
                    # newSpeaker = Speaker(first_name=fileSpeakerFirst, last_name=fileSpeakerLast, user_id=None)
                    # newSpeaker.save()
                    # fileSpeakerId = newSpeaker

            if not os.path.isfile(settings.MEDIA_ROOT + 'user_' + str(request.user.id) + '_big/' + str(fileFile)):
                big_audio = BigAudio(sound_file=fileFile, length = fileLength, owner_id=fileOwner, speaker_id=fileSpeakerId, language_id=fileLanguageId)
                big_audio.save()
                active_messages["trimAudio"] = 'user_' + str(request.user.id) + '_big/' + str(fileFile)
            else:
                active_messages["trimAudio"] = 'File with that name already exists'
                #return redirect('/uploadAudio/')
            # print(settings.MEDIA_ROOT + 'user_' + str(request.user.id) + 'big/' + str(fileFile))
            # print(active_messages["trimAudio"])
            # print(settings.MEDIA_ROOT + active_messages["trimAudio"])
            active_messages["trimAudio"] = 'File succesfully uploaded'
            return redirect('/trimAudio/')
        else:
            redirect('/uploadAudio/')
    else:
        redirect('/uploadAudio/')

#end of ajax calls


# start of other functions
@csrf_exempt
def set_password(user, newPass):
    if is_user_type(request, 'auth_user'):
        u = User.objects.get(username=user)
        u.set_password(newPass)
        u.save()
