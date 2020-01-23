from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
# from .models import ## TODO: Add DB tables

# Create your views here.
def display_home(request):
    return render(request, 'general/HomePage.html') ## TODO: change to index.html

def display_create(request):
    return render(request, '## TODO: ')

def display_dash(request):
    return render(request, '## TODO: ')

def display_data(request):
    return render(request, '## TODO: ')

def logout_view(request):
    return render(request)

@csrf_exempt
def post_data(request):
    if request.method == 'POST':
        pass

@csrf_exempt
def ajax_getStats(request):
    if request.method == 'GET':
        pass
