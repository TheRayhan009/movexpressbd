from django.shortcuts import render ,redirect
from django.http import HttpResponse ,JsonResponse
import random


def home(request):
    log = request.session.get("log")

    return render(request, 'home.html')

def order(request):
    log = request.session.get("log")

    return render(request, 'order.html')

def founderrayhan(request):
    log = request.session.get("log")

    return render(request, 'rayhan.html')

def founderarafat(request):
    log = request.session.get("log")

    return render(request, 'arafat.html')