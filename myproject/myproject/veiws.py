# from django.http import Httpresponse
from django.shortcuts import render

def homepage(request):
    # return Httpresponse("hello world! i'm home.")
    return render(request, 'home.html')

def about(request):
    # response("my about page.")
    return render(request, 'about.hmtl')