from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello Everybody welcome to Home page")
    return render(request, 'website/index.html')


def about(request):
    # return HttpResponse("Hello Everybody welcome to about page")
    return render(request, 'website/index2.html')

def contact(request):
    return HttpResponse("Hello Everybody welcome to contact page.")