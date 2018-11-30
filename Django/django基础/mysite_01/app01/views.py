from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'base.html', {"name": "张亚瀚"})


def yimi(request):
    return HttpResponse('薏米')


def xiaohei(request):
    return HttpResponse('小黑')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        print(password)
        return HttpResponse('OK')