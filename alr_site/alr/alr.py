from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import AudioTrim


def GetAllAudioTrim():
    all_trims = AudioTrim.objects.all()
    all_audio_trims = encoder_JSON(all_trims)#, all_trims.attributes)
    return all_audio_trims

def encoder_JSON(data):
    response = {}
    for key in data:
        obj = []
        obj.append(key.original_text)
        response[key.id] = obj
    return response
