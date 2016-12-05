from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponseRedirect

from django import forms
#from django.forms import NameForm

def index(request):
    return render(request, 'personal/home.html') 

@csrf_exempt
def play(request):
    if request.method == 'POST':
        print(request.POST)
        form = request.method(request.POST)
       winner = play('rock')
    return render(request, 'personal/winner.html')

# 127.0.0.1:800/personal
