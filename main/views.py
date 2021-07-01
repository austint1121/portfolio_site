from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.core.mail import send_mail

from main.forms import ContactForm
from django.http import HttpResponseRedirect
# Create your views here.
def emailform(request):
    """For when a contact form is submitted; this will redirect to the email_success view."""
    form = ContactForm(request.POST)
    if form.is_valid():
        user_name = form.cleaned_data['name']
        user_email = form.cleaned_data['email']
        user_message = form.cleaned_data['message']
        subject = f"Message from '{user_name}' via mturner.me Contact Form"
        message = user_message + f'\n\nReply email is {user_email}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['austin.turner1121@gmail.com']
        send_mail(subject, message, email_from, recipient_list)
        return redirect('/index/success/')

def index(request):
    """View for the Index of the site."""
    if request.method =='POST':
       emailform(request)
    form = ContactForm()
    context = {
        'form':form
    }
    return render(request, 'index.html', context)

def email_success(request):
    """View for when a contact form is filled out and successfully sent via email."""
    form = ContactForm()
    context = {
        'form':form
    }
    return render(request, 'email_sent.html', context)

def about_me(request):
    """View for About me page"""
    if request.method =='POST':
        emailform(request)
    form = ContactForm()
    context = {
        'form':form
    }
    return render(request, 'about_me.html', context)

def contact(request):
    """View for the Contact page."""
    if request.method =='POST':
        emailform(request)
    form = ContactForm()
    context = {
        'form':form
    }
    return render(request, 'contact.html', context)

def projects(request):
    """View for the Projects page."""
    if request.method =='POST':
        emailform(request)
    form = ContactForm()
    context = {
        'form':form
    }
    return render(request, 'projects.html', context)