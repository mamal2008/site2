from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index(request):
    return render(request,'site2/index.html')

def contact(request):
    return render(request,'site2/contact.html')

def blog(request):
    return render(request,'site2/blog.html')

def about(request):
    return render(request,'site2/about.html')
