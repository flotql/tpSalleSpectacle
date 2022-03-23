from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.

class TypeOfEvents(models.Model):
    type_of_event_name = models.CharField(max_length=50)

class Artists(models.Model):
    artist_name = models.CharField(max_length=30)
    artist_firstname = models.CharField(max_length=30, blank=True, null=True)

class WhoIsHere(models.Model):
    who_is_here_name = models.CharField(max_length=30)
    have = models.ManyToManyField(Artists)
    
    def __str__(self):
        return who_is_here_name

class Schedule(models.Model):
    start_date = models.DateTimeField('date de début')
    end_date = models.DateTimeField('date de fin')

class TyOfShowroom(models.Model):
    type_of_showroom_name = models.CharField(max_length=50)

class Events(models.Model):
    event_name = models.CharField(max_length=50)
    event_start_date = models.DateTimeField('date de début')
    event_end_date = models.DateTimeField('date de fin')
    type_of_event = models.ForeignKey(TypeOfEvents, on_delete=models.CASCADE)
    book = models.ManyToManyField(User, blank=True)
    perform = models.ManyToManyField(WhoIsHere)
    prepare = models.ManyToManyField(Schedule, blank=True)

class Showroom(models.Model):
    showroom_name = models.CharField(max_length=30)
    showroom_places = models.IntegerField(default=0)
    events = models.ForeignKey(Events, on_delete=models.CASCADE)
    tyofshowroom = models.ForeignKey(TyOfShowroom, on_delete=models.CASCADE)