from django.contrib import admin
from .models import TypeOfEvents, Artists, WhoIsHere, Schedule, TyOfShowroom, Events, Showroom


# Register your models here.

admin.site.register(TyOfShowroom)
admin.site.register(Artists)
admin.site.register(WhoIsHere)
admin.site.register(TypeOfEvents)
admin.site.register(Schedule)
admin.site.register(Events)
admin.site.register(Showroom)
