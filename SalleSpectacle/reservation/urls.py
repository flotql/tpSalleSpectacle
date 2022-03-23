from django.urls import path
from . import views

app_name = 'reservation'

urlpatterns= [
    path('', views.index, name='index'),

    # path('<int:pk>/', views.the_event.as_view(), name='the_event'),


]
