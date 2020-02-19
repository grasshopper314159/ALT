from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import AudioTrim


def GetAllAudioTrim(request):
    all_trims = AudioTrim.objects.all()
    all_audio_trims = encoder_JSON(all_trims, request)#, all_trims.attributes)
    return all_audio_trims

def encoder_JSON(data, request):
    response = {}
    for key in data:
        obj = []
        # id = models.AutoField(unique=True, primary_key=True)
#         big_audio_id = models.ForeignKey("BigAudio", on_delete=models.CASCADE, default=None)
#         original_text = models.TextField()
#         english_text = models.TextField()
#         phonetic_text = models.TextField(default=None, blank=True, null=True)
#         comments = models.ManyToManyField("User", through="Comment", related_name="big_audio_comments") # User and big audio 'can comment' relationship
#         last_listened_date = models.DateTimeField(default=None, blank=True, null=True)
#         score = models.IntegerField(default=None, blank=True, null=True)
#         word_count = models.IntegerField(default=None, blank=True, null=True)
#         # Length should probably be required
#         length = models.IntegerField(default=None, blank=True, null=True)
#         start_time = models.TimeField()

        if (key.big_audio_id.owner_id == request.user.id):
            obj.append(key.big_audio_id.owner_id.id.first_name, ' ', key.big_audio_id.owner_id.id.last_name)
            obj.append(key.speaker_id.first_name, ' ', key.speaker_id.last_name)
            obj.append(key.original_text)
            obj.append(key.english_text)
            obj.append(key.score)
            obj.append(key.last_listened_date)

            response[key.id] = obj

    return response
