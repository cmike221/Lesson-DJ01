from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    # return HttpResponse("<h1>Это мой первый проект на Django</h1>")
    datas = {
        'caption': "MountDjango"
    }
    return render(request, 'main/index.html', datas)


def page2(request):
    return render(request, 'main/page2.html')


def page3(request):
    return render(request, 'main/page3.html')


def page4(request):
    return render(request, 'main/page4.html')
