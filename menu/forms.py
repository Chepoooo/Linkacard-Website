from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    business = forms.CharField(max_length=200, label="Business / Purpose")
    email = forms.EmailField(label="Email")