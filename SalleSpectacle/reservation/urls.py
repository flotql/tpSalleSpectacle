from django.urls import path
from . import views

app_name = 'reservation'

urlpatterns= [
    path('', views.index, name='index'),
    path('<int:event_id>/', views.the_event, name='the_event'),
    path('<int:event_id>/purchase', views.ticket_purchase, name='purchase'),
    path('profil/', views.profil, name='profil'),
    path('artists/<int:event_id>', views.artists, name='artists'),
    path('profil/detail/<int:event_id>', views.detail, name='detail'),
    path('profil/detail/cancel/<int:event_id>', views.cancel, name='cancel'),
    path('login/', views.my_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.my_logout, name='logout'),
    path ('registered/', views.registered, name='registered'),
    path ('welcome/', views.welcome, name='welcome'),
    path ('purchase/', views.ticket_purchase, name='purchase'),
    path('password/', views.password, name='password'),
    path('password/passwordValidation', views.passwordValidation, name='passwordValidation')
]
