from django.shortcuts import render
from django.http import HttpResponse

def test(request, *args, **kwargs):
    return HttpResponse('OK.\n' + str(request) + '\n' + str(args) + '\n' + str(kwargs))