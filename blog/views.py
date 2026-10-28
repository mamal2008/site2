from django.shortcuts import render

def blog(request):
    return render(request,'blog/blog.html')
def blog_ex(request):
    return render(request,'blog/ex.html')