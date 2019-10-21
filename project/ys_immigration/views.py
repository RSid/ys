from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def waiting(request):
    return render(request, 'ys_immigration/with-you-shortly.html')

def ycis_home(request):
    return render(request, 'ys_immigration/home.html')
