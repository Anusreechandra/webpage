from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.


def new(request):
    return render(request,'web.html')