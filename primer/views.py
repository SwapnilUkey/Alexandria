# Alexandria/primer/views.py
from django.http import HttpResponse
from django.shortcuts import render


def say_hello(request):
    message = "Hello World!"

    return HttpResponse(message, content_type="text/plain")
