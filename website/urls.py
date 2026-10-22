from django.urls import path
from website.views import about,index,contact,blog

app_name='website'
urlpatterns=[
    path('home',index,name='home'),
    path('about',about,name='about'),
    path('blog',blog,name='blog'),
    path('home',contact,name='contact')
]