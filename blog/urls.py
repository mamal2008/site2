from django.urls import path
from blog.views import *

app_name='blog'

urlpatterns=[
    path('',blog,name='Ublog'),
    path('ex',blog_ex)
]
