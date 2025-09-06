from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            business = form.cleaned_data["business"]
            email = form.cleaned_data["email"]

            # Construcción del mensaje
            subject = f"Nuevo mensaje de contacto - {name}"
            message = f"""
            Nombre: {name}
            Negocio/Propósito: {business}
            Email: {email}
            """
            
            # Enviar el correo
            send_mail(
                subject,
                message,
                email,  
                ["luismc.tellex@gmail.com"],  
            )

           
            messages.success(request, "✅ Message Sent Successfully! Will get back to you soon.")
            return redirect("contact")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})

def order(request):
    return render(request, 'order.html')
