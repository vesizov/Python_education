from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def me(request):
    return render(request, 'generator/me.html')


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend([up_char.upper() for up_char in characters])

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    length = int(request.GET.get('length', 12))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    the_password = ''

    for s in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})
