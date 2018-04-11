from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from . models import Projects


# Create your views here.
def index(request):
    
    portfolio = Projects.objects.all()
    return render(request,"index.html", {'portfolio':portfolio})