from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from random import randint


# Create your views here.
def rnd():
    return randint(1000000, 10000000)
    
def index(request):
    latest_event_list = Events.objects.order_by('id')
    context = {'event_list': latest_event_list}
    return render(request, 'reservation/index.html', context)

def the_event(request, event_id):
    event = get_object_or_404(Events, pk=event_id)
    places = event.take.all()
    total = 0
    for i in places:
        total += i.showroom_places
    total -= event.sold_places
    # total = sum([i.showroom_places for i in places]) - event.sold_places
    return render(request, 'reservation/the_event.html', {'event':event, 'total':total})

def ticket_purchase(request, event_id):
    event = Events.objects.get(pk=event_id)
    event.book.add(request.user)
    event.sold_places +=1
    event.save()
    context = {'event':event }
    return render(request, 'reservation/purchase.html', context)

def artists(request, event_id):
    artist = get_object_or_404(WhoIsHere, pk=event_id)
    return render(request, 'reservation/artists.html', {'artist':artist})

def profil(request):
    nomEvent = []
    for list_event in Events.objects.all():
        for user_list in list_event.book.all():
            if user_list == request.user:
                nomEvent.append(list_event)
    context = {'nomEvent':nomEvent}
    return render(request, 'reservation/profil.html', context)

def detail(request,event_id):
    event = get_object_or_404(Events, pk=event_id)
    return render(request, 'reservation/detail.html', {'event':event, 'rnd':rnd()})


def cancel(request,event_id):
    event = Events.objects.get(pk=event_id)
    event.book.remove(request.user)
    event.sold_places -=1
    event.save()
    context = {'event':event }
    return render(request, 'reservation/cancel.html', context)

def my_login(request):
    return render(request, 'reservation/login.html')

def welcome(request):
    username = request.POST['user_name']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    context = {'user':user}
    if user is not None:
        login(request, user)
        return render(request, 'reservation/welcome.html', context)
    else :
        return render(request, 'reservation/error_log.html')

def my_logout(request):
    logout(request)
    return render(request, 'reservation/logout.html')

def register(request):
    return render(request, 'reservation/register.html')

def registered(request):
    name = request.POST['user_name']
    firstname = request.POST['user_firstname']
    pwd = request.POST['user_pwd']
    email = request.POST['user_email']
    username = firstname[0].lower() + "." + name.lower()
    user = User.objects.create_user(username, email, pwd)
    context = {'user':user}
    return render(request, 'reservation/registered.html', context)

def password(request):
    return render(request, 'reservation/password.html')

def passwordValidation(request):
    new_pw = request.POST['password']
    pw = User.objects.get(username=request.POST['user_name'])
    pw.set_password(new_pw)
    pw.save()
    return render(request,'reservation/passwordValidation.html',)
