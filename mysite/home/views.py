from django.shortcuts import render,HttpResponse
from  datetime import datetime
from home.models import Contact
from django.contrib import messages

def index(request):
    context = {
        'code':223222

    } 
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

#  return HttpResponse('this is aboutpage')

def service(request):
#  return HttpResponse('this is servicespage') 
  return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        if email:
            contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
            contact.save()
            messages.success(request, 'your message has been sent.')
            return render(request, 'contact.html')
    return render(request, 'contact.html')


# Create your views here.
