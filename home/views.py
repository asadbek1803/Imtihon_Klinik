from django.shortcuts import render

# Create your views here.



def home(request): # Asosiy page uchun

    return render(request, "index.html")


def Error404(request): # Mavjud emas Page
    return render(request, "404.html")

def about(reqeust): # About page

    return render(reqeust, "about.html")

def contact(reqeust): # Contact Page

    return render(reqeust, "contact.html")

def feature(request): # Feature Page

    return render(request, "feature.html")

def appointment(reqeust): # Appointment page

    return render(reqeust, "appointment.html")

def team(request): # Team page

    return render(request, "team.html")

def service(request): # Service page

    return render(request, "service.html")

def testimonial(request): # Testimonial page

    return render(request, "testimonial.html")
