from django.http import HttpResponse
from django.shortcuts import render
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list('qwertyuiopasdfghjklzxcvbnm')
    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+=-*?:%;№"'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    lenght = int(request.GET.get('lenght', 9))
    thepassword = ''


    for x in range(lenght):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html',{'password':thepassword})