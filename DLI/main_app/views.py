from django.shortcuts import render
from django.http import HttpResponse
from .Functions import script
# Create your views here.

def test(request, mRange):
    response = script.numbers_to_add(mRange)
    return HttpResponse(response)