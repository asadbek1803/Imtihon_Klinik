from django.shortcuts import render, redirect
from .models import Statics, Album_home, About_Us, Services, Features, Doctors, Appointment, Testimonial
# Create your views here.
from django.contrib.auth import logout, login, authenticate



def logout_u(request):
    logout(request)
    return redirect("/login/")

def login_u(request):
    if request.POST:
        name = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=name, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "login.html", {"error": "Login yoki parol xato"})



    return render(request, "login.html")

def home(request): # Asosiy page uchun

    if request.user.is_authenticated:
        if request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            doctor = request.POST.get('doctors')
            date = request.POST.get('date')
            datetime = request.POST.get('time')
            about = request.POST.get('message')

            Appointment.objects.create(name=name, email=email, phone=phone, doctor=doctor, date=date, datetime=datetime, about=about)



        data = {
            "Statics": Statics.objects.all(),
            "albums": Album_home.objects.all(),
            "about_us": About_Us.objects.all(),
            "services": Services.objects.all(),
            "features": Features.objects.all(),
            'teams': Doctors.objects.all(),
            "testimonials": Testimonial.objects.all()

        }
        return render(request, "index.html", data)
    else:
        return redirect("/login/")

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
