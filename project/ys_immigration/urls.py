from django.urls import path

from . import views

urlpatterns = [
    path('', views.waiting, name='waiting'),
    path('home', views.ycis_home, name='home')
]
