from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import Message

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def events(request):
    return render(request, 'events.html')


def pricing(request):
    return render(request, 'pricing.html')


def events(request):
    return render(request, 'events.html')


def courses(request):
    return render(request, 'courses.html')


def trainers(request):
    return render(request, 'trainers.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get('message')

        messageSave = Message(name=name, email=email, subject=subject, message = message )
        messageSave.save()

        return redirect("/")
    
        
    return render(request, 'contact.html')
