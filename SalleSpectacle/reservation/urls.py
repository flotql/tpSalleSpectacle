from django.urls import path
from . import views

app_name = 'reservation'

urlpatterns= [
    path('', views.index, name='index'),
    path('<int:event_id>/', views.the_event, name='the_event'),
    path('<int:event_id>/purchase', views.ticket_purchase, name='purchase'),
]
