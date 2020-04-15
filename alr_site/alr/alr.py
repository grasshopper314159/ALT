from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

# import all db tables
from .models import User, BigAudio, Speaker, Language, Review, AudioTrim, Comment, Measurements, Class, Assignment

# TODO all_trims should only retrieve trims accessible by current user.
def getAllAudioTrim(request):
    all_trims = AudioTrim.objects.all()

    # This is linear to the number of total audio_trims (i.e. might get slow?)
    response = {}
    for key in all_trims:
        obj = {}
        # TODO: change so you can see data of other people who allow you access
        if (key.big_audio_id.owner_id.id == request.user):
            obj['owner'] = key.big_audio_id.owner_id.id.first_name + ' ' + key.big_audio_id.owner_id.id.last_name
            obj['speaker'] = key.big_audio_id.speaker_id.first_name + ' ' + key.big_audio_id.speaker_id.last_name
            obj['original_text'] = (key.original_text)
            obj['english_text'] = (key.english_text)
            obj['score'] = (key.score)
            obj['date'] = (key.last_listened_date)
            # key.id is the primary key for a given audio trim
            response[key.id] = obj

    return response

def getAllLanguages(request):
    all_Languages = Language.objects.all()

    # This is linear to the number of total audio_trims (i.e. might get slow?)
    response = {}
    for key in all_Languages:
        response[key.id] = key.name

    return response

def getAllAudioByID(request):
    id = request.POST.data.id
    Audio = BigAudio.objects.get(id=id)

    # This is linear to the number of total audio_trims (i.e. might get slow?)
    response = {}
    response['id'] = Audio.id
    response['upload_date'] = Audio.upload_date
    response['sound_file'] = Audio.sound_file
    response['length'] = Audio.length
    response['owner_id'] = Audio.owner_id
    response['speaker_id'] = Audio.speaker_id
    response['language_id'] = Audio.language_id
    response['reviews'] = Audio.reviews
    response['private'] = Audio.private

    return response

getAllAudioByID


def getEval(request):
    pass

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

def updateRating(request):
    trim = AudioTrim.objects.filter(id=request.POST['trim_id'])
    trim.score = request.POST['score']
    trim.save()
