from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from step.models import *

from django.shortcuts import render_to_response
from pyasn1.type.univ import Null, NoValue
from django.template.defaultfilters import date
import datetime
from django import forms


def index(request):
    return render(request,'index.html')


def choose(request):

    context = {}  

    Time1 = request.POST['time']

    Basic1 = request.POST.get('basic1')
    if Basic1 == 'on':
      Basic1 = True

    Electrical1 = request.POST.get('electrical1')
    if Electrical1 == 'on':
      Electrical1 = True

    Mechanical1 = request.POST.get('mechanical1')
    if Mechanical1 == 'on':
      Mechanical1 = True

    Installation1 = request.POST.get('installation1')
    if Installation1 == 'on':
      Installation1 = True

    Water1 = request.POST.get('water1')
    if Water1 == 'on':
      Water1 = True

    Option.objects.create(Time=Time1, Basic1=Basic1, Electrical1=Electrical1, Mechanical1=Mechanical1, Installation1=Installation1, Water1=Water1)  

    bas = Option.objects.all().values_list('Basic1', flat=True).last()
    ele = Option.objects.all().values_list('Electrical1', flat=True).last()
    mec = Option.objects.all().values_list('Mechanical1', flat=True).last()
    ins = Option.objects.all().values_list('Installation1', flat=True).last()
    wat = Option.objects.all().values_list('Water1', flat=True).last()

    context = {"bas": bas, "ele": ele, "mec": mec, "ins": ins, "wat": wat}

    return render(request, "index2.html", context)
    


def ask(request):

    context = {}
    
    Basic = request.POST.get('basic')
    Electrical = request.POST.get('electrical')
    Mechanical = request.POST.get('mechanical')
    Installation = request.POST.get('installation')
    Water = request.POST.get('water')
    Username = request.POST['name']

    Detail.objects.create(Basic=Basic, Electrical=Electrical, Mechanical=Mechanical, Installation=Installation, Water=Water, Name=Username)   
    
    listing = Detail.objects.all()
    context = {"listing":listing}

    return render(request, "display.html", context)
    