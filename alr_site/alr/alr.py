from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

# import all db tables
from .models import User, BigAudio, Speaker, Language, Review, AudioTrim, Comment, Measurements, Class, Assignment

# TODO: add all fields from models.py

# used by view audio and rate audio
def getAllAudioTrim(request, admin=False):
    ratable = request.GET['ratable']

    all_trims = AudioTrim.objects.all()

    # This is linear to the number of total audio_trims (i.e. might get slow?)
    response = {}
    for key in all_trims:
        obj = {}
        # TODO: change so you can see data of other people who allow you access

        # for view if not admin
        if not admin and not ratable and key.big_audio_id.owner_id.id == request.user:
            obj['owner'] = key.big_audio_id.owner_id.id.first_name + ' ' + key.big_audio_id.owner_id.id.last_name
            obj['speaker'] = key.big_audio_id.speaker_id.first_name + ' ' + key.big_audio_id.speaker_id.last_name
            obj['original_text'] = (key.original_text)
            obj['english_text'] = (key.english_text)
            obj['score'] = (key.score)
            obj['date'] = (key.last_listened_date)
            obj['url'] = key.big_audio_id.sound_file.url
            response[key.id] = obj

        # for rate audio if not admin
        elif not admin and ratable:
            if key.score == None:
                obj['owner'] = key.big_audio_id.owner_id.id.first_name + ' ' + key.big_audio_id.owner_id.id.last_name
                obj['speaker'] = key.big_audio_id.speaker_id.first_name + ' ' + key.big_audio_id.speaker_id.last_name
                obj['original_text'] = (key.original_text)
                obj['english_text'] = (key.english_text)
                obj['score'] = (key.score)
                obj['date'] = (key.last_listened_date)
                obj['url'] = key.big_audio_id.sound_file.url
                response[key.id] = obj


        # admin gets to see all trims
        elif admin:
            obj['owner'] = key.big_audio_id.owner_id.id.first_name + ' ' + key.big_audio_id.owner_id.id.last_name
            obj['speaker'] = key.big_audio_id.speaker_id.first_name + ' ' + key.big_audio_id.speaker_id.last_name
            obj['original_text'] = (key.original_text)
            obj['english_text'] = (key.english_text)
            obj['score'] = (key.score)
            obj['date'] = (key.last_listened_date)
            obj['url'] = key.big_audio_id.sound_file.url

            # key.id is the primary key for a given audio trim
            response[key.id] = obj
    return response

def getAllLanguages(request):
    all_Languages = Language.objects.all()
    response = {}
    for key in all_Languages:
        response[key.id] = key.name
    return response

# TODO: This is for a simple signin where the reshearcher has created the account that the rater will use
# TODO: the creation of these account is not yet implemented
def createEval(request, active_messages):
    trims = request.POST['trims']
    firstname = request.POST['eval_firstname']
    lastname = request.POST['eval_lastname']
    email = request.POST['email']
    pin = request.POST['eval_pin']

    username = firstname + "." + lastname
    user_type = 'eval_user'

    user = authenticate(request=None, username=username, password=pin)
    try:
        if user is None:
            # create django user
            user_acc = User.objects.create_user(username, email, pin, first_name=firstname, last_name=lastname) #, groups=Group.)
            user_acc.save()
            user_acc.groups.add(name='auth_user')
            user_acc.groups.add(name=str(user_type))
            user_acc.save()

            # create alr user
            u = alr_user(id=user_acc, type=user_type)
            u.save()
            return 'You have created an account for ' + firstname + ' ' + lastname + '.<br>' + 'their Username is ' + firstname + '.' + lastname + ' and their password is the pin you provided.<br>' + 'the URL for them is alr.hs.umt.edu/eval/login/'
        else:
            return 'Their is already and account for ' + firstname + ' ' + lastname + '.'
    except Exception as e:
        if str(e) == 'UNIQUE constraint failed: auth_user.username':
            return 'Their is already and account for ' + firstname + ' ' + lastname + '.'
        else:
            return e

# TODO: currently only updates ratings should also update comments
def updateRating(request):
    trim = AudioTrim.objects.get(id=int(request.POST['trim_id']))
    trim.score = request.POST['value']
    trim.save()
