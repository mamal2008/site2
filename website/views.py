from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index(request):
    render(request,'site2/index.html')

def contact(request):
    render(request,'site2/contact.html')

def blog(request):
    render(request,'site2/blog.html')

def about(request):
    render(request,'site2/about.html')
