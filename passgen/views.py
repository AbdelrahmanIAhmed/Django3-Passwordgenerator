from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'passgen/home.html', { 'password': 'ksjgkjskgjk'})

def password(request):

    characters = list('abcdefgholmnvxyzqpjklpiutrw')
    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPLKJHGFDSAZXCVBNM'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))
        
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int (request.GET.get('length',12))
    the_password= ''
    for x in range (length):

        the_password += random.choice(characters)

    return render(request,'passgen/password.html',{'mypass': the_password})

def about(request):

    return render(request,'passgen/about.html')