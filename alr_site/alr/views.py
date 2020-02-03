from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from alr.models import AudioTrim

# Create your views here.
def display_data(request):
    all_audio_trims = AudioTrim.objects.all()
    context = {'all_audio_trims':all_audio_trims}
    return render(request, 'public/ViewData.html')

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
