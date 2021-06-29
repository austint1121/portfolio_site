from django import forms
from django.forms import Textarea


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', required=True, initial='Name')
    email = forms.EmailField(label='Email', required=True, initial='Email')
    message = forms.CharField(widget=Textarea, required=True, label='Message', initial='Message')