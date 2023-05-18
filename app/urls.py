from django.urls import path

app_name='app'

from app.views import *

urlpatterns=[

    path('venky/',venky,name='venky'),

]