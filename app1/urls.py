from django.urls import path

app_name='app1'

from app1.views import *
urlpatterns=[

    path('venkydare/',venkydare,name='venkydare'),

]