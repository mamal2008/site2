from django.urls import path
from website.views import about,index,contact

app_name='website'
urlpatterns=[
    path('home',index,name='home'),
    path('about',about,name='about'),
    path('contact',contact,name='contact')
]