from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('主页')


def yimi(request):
    return HttpResponse('薏米')


def xiaohei(request):
    return HttpResponse('小黑')
