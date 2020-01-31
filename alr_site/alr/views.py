from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
# from .models import ## TODO: Add DB tables

# Create your views here.
def display_home(request):
    return render(request, 'public/index.html') ## TODO: change to index.html

def display_aboutUs(request):
    return render(request, 'public/AboutUs.html')

def display_signUp(request):
    return render(request, 'public/SignUp.html')

def display_data(request):
    return render(request, '## TODO: ')

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
