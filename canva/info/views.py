from django.shortcuts import render,redirect
from .models import Contact
def home(request):
    return render(request, "index.html") 
def contact(request):
    return render(request,'contact.html')

def confirm_contact(request):
    if request.method=='GET':
        return redirect('info:contact')
    elif request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        phone=request.POST.get('phone')
        contact=Contact(name=name,email=email,message=message,phone=phone)
        contact.save()
        return redirect('info:contact')