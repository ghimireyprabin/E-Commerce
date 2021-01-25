from django.urls import path
from .views import *

urlpatterns=[

    path('',index,name="index"),
    path('services',service,name="service"),
    path('contact',contact,name="contact")
]