from django.shortcuts import render,redirect
from .models import Addmision
from django.contrib import messages
# Create your views here.


def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        PhoneNumber = request.POST.get('PhoneNumber')
        Email = request.POST.get('Email') 
        State = request.POST.get('State') 
        course = request.POST.get('course') 
        obj = Addmision.objects.create(name=name,phono=PhoneNumber,email=Email,state=State,course=course)
        obj.save()
        messages.success(request, 'Registration completed successfully.')
        return redirect('home')

    return render(request,'index.html')

