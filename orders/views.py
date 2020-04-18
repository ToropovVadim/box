from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'project/index.html')


def index_test(request):
    return render(request, 'index_test.html')


def index_testt(request):
    return render(request, 'index_testt.html')
