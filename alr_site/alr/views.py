from django.shortcuts import render
from django.contrib.auth import logout
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from alr.models import AudioTrim

# Create your views here.
def display_viewData(request):
    return render(request, 'general/ViewData.html')

def display_home(request):
    return render(request, 'public/index.html') ## TODO: change to index.html

def display_aboutUs(request):
    return render(request, 'public/AboutUs.html')

def display_signUp(request):
    return render(request, 'public/SignUp.html')

def logout_view(request):
    return render(request)

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...

@csrf_exempt
def post_data(request):
    if request.method == 'POST':
        pass

@csrf_exempt
def ajax_getStats(request):
    if request.method == 'GET':
        pass

# function for ajax, returns json object with all audio trims
@csrf_exempt
def ajax_getAllAudioTrims(request):
    if request.method == 'GET':
        return JsonResponse(GetAllAudioTrim(), safe=False)


def GetAllAudioTrim():
    all_audio_trims = serialize('json', AudioTrim.objects.all(), cls=LazyEncoder)
    response = {'all_audio_trims':all_audio_trims}
    return response

# copied from https://docs.djangoproject.com/en/3.0/topics/serialization/#serialization-formats-json
from django.core.serializers.json import DjangoJSONEncoder

class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, AudioTrim):
            return str(obj)
        return super().default(obj)
