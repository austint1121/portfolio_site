from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.core.mail import send_mail

from main.forms import ContactForm
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    if request.method =='POST':
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
            return redirect('success/')
    else: form = ContactForm()
    context = {
        'form':form
    }
    return render(request, 'index.html', context)

def email_success(request):
    form = ContactForm()
    context = {
        'form':form
    }
    return render(request, 'email_sent.html', context)