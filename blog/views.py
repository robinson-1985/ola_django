from django.shortcuts import render
from django.http import HttpResponse


def blog(request):
    print('blog')
    return HttpResponse('Hello from blog!')
