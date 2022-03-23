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


# Create your views here.

def index(request):
    latest_event_list = Events.objects.order_by('id')
    context = {'event_list': latest_event_list}
    return render(request, 'reservation/index.html', context)

def the_event(request, event_id):
    event = get_object_or_404(Events, pk=event_id)
    return render(request, 'reservation/the_event.html', {'event':event})

def ticket_purchase(request, event_id):
    return HttpResponse("Mes billets")

def profil(request):
    pass
    # asso = Events.book.objects.
    # return render(request, 'reservation/profil.html')

def cancel(request,event_id):
    event = Events.objects.get(pk=event_id)
    asso = event.book.get(request, username='user_id')
    asso.delete()
    context = {'event':event }
    return render(request, 'reservation/cancel.html', context)
    return render(request, 'reservation/profil.html')

# Vues pour l'inscription /le login/ et le logout d'un utilisateur
def my_login(request):
    return render(request, 'reservation/login.html')

def register(request):
    return render(request, 'reservation/register.html')

def my_logout(request):
    logout(request)
    return render(request, 'reservation/logout.html')

def registered(request):
    name = request.POST['user_name']
    firstname = request.POST['user_firstname']
    pwd = request.POST['user_pwd']
    email = request.POST['user_email']
    username = firstname[0].lower() + "." + name.lower()
    user = User.objects.create_user(username, email, pwd)
    context = {'user':user}
    return render(request, 'reservation/registered.html', context)

def welcome(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    context = {'user':user}
    if user is not None:
        login(request, user)
        return render(request, 'reservation/welcome.html', context)
    else :
        return render(request, 'reservation/error_log.html')


