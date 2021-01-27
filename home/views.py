from django.shortcuts import render,HttpResponse
from home.models import Contact
from datetime import datetime
from django.db import models

from django.contrib import messages

# Create your views here.
def index(request):

       
    return render(request,'home\index.html')  

def service(request):
    return render(request,'home\services.html')
    #return HttpResponse("this is services")
def contact(request):

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        contact=Contact(name=name,email=email,phone=phone)
       
        try:
            contact.full_clean()
            print(contact.full_clean())
            contact.save()
            messages.success(request, 'Your form has been submited')
        except:

            messages.warning(request, 'Validation error')

        

        


        
           


           




        

     

        
        
    return render(request,'home\contact.html')
    #return HttpResponse("this is contact")    