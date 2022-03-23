from django.urls import path
from . import views

app_name = 'reservation'

urlpatterns= [
    path('', views.index, name='index'),
    path('<int:pk>/', views.the_event, name='the_event'),
]
