from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.

def cabinet(request):
    all_keys = Key.objects.all()
    return render(request, 'cabinet.html', {'keys': all_keys})