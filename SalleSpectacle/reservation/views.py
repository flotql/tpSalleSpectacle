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


