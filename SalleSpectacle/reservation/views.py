from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
    return render(request, 'reservation/index.html')

def the_event(request):
    return render("Les concerts")

def ticket_purhcase(request):
    return HttpResponse("Mes billets")

