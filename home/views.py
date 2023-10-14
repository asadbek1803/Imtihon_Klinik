from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Statics, Album_home, About_Us, Services, Features,Contact, Doctors, Appointment, Testimonial
# Create your views here.
from django.contrib.auth import logout, login, authenticate
# from .forms import AddDoctorForm


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


def home(request):  # Asosiy page uchun

    if request.user.is_authenticated:
        if request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            doctor = request.POST.get('doctors')
            date = request.POST.get('date')
            datetime = request.POST.get('time')
            about = request.POST.get('message')

            Appointment.objects.create(name=name, email=email, phone=phone, doctor=doctor, date=date, datetime=datetime,
                                       about=about)

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


def Error404(request):  # Mavjud emas Page
    return render(request, "404.html")


def about(reqeust):  # About page
    data = {
        "Statics": Statics.objects.all(),
        "albums": Album_home.objects.all(),
        "about_us": About_Us.objects.all(),
        "services": Services.objects.all(),
        "features": Features.objects.all(),
        'teams': Doctors.objects.all(),
        "testimonials": Testimonial.objects.all()

    }

    return render(reqeust, "about.html", data)


def contact(reqeust):  # Contact Page
    if reqeust.POST:
        name = reqeust.POST.get('name')
        email = reqeust.POST.get('email')
        subject = reqeust.POST.get('subject')
        message = reqeust.POST.get('message')

        Contact.objects.create(name=name, email=email, subject=subject, message=message)


    return render(reqeust, "contact.html")


def feature(request):  # Feature Page
    data = {
        "Statics": Statics.objects.all(),
        "albums": Album_home.objects.all(),
        "about_us": About_Us.objects.all(),
        "services": Services.objects.all(),
        "features": Features.objects.all(),
        'teams': Doctors.objects.all(),
        "testimonials": Testimonial.objects.all()

    }

    return render(request, "feature.html", data)


def appointment(reqeust):
    # Appointment page
    data = {
        "Statics": Statics.objects.all(),
        "albums": Album_home.objects.all(),
        "about_us": About_Us.objects.all(),
        "services": Services.objects.all(),
        "features": Features.objects.all(),
        'teams': Doctors.objects.all(),
        "testimonials": Testimonial.objects.all()

    }
    return render(reqeust, "appointment.html", data)


def team(request):  # Team page
    if request.POST:
        name = request.POST.get('full_name')
        image = request.POST.get('image')
        staff_name = request.POST.get('staff_name')
        facebook = request.POST.get('facebook')
        twitter = request.POST.get('twitter')
        instagram = request.POST.get('instagram')

        Doctors.objects.create(image=image, full_name=name, staff_name=staff_name, facebook=facebook, twitter=twitter, instagram=instagram)

        # form = AddDoctorForm(request.POST)


        # image = request.POST.get('image')
        #
        # name = request.POST.get('name')
        #
        # staff_name = request.POST.get('staff_name')
        # facebook = request.POST.get('facebook')
        # twitter = request.POST.get('twitter')
        # instagram = request.POST.get('instagram')
        #
        # Doctors.objects.create(image=image, full_name=name, staff_name=staff_name, facebook=facebook,
        #                            twitter=twitter, instagram=instagram)




    data = {
        "Statics": Statics.objects.all(),
        "albums": Album_home.objects.all(),
        "about_us": About_Us.objects.all(),
        "services": Services.objects.all(),
        "features": Features.objects.all(),
        'teams': Doctors.objects.all(),
        "testimonials": Testimonial.objects.all(),


    }

    return render(request, "team.html", data)


def service(request):  # Service page
    if request.user.is_authenticated:
        if request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            doctor = request.POST.get('doctors')
            date = request.POST.get('date')
            datetime = request.POST.get('time')
            about = request.POST.get('message')

            Appointment.objects.create(name=name, email=email, phone=phone, doctor=doctor, date=date, datetime=datetime,
                                       about=about)

        data = {
            "Statics": Statics.objects.all(),
            "albums": Album_home.objects.all(),
            "about_us": About_Us.objects.all(),
            "services": Services.objects.all(),
            "features": Features.objects.all(),
            'teams': Doctors.objects.all(),
            "testimonials": Testimonial.objects.all()

        }

        return render(request, "service.html", data)


def testimonial(request):  # Testimonial page
    data = {
        "Statics": Statics.objects.all(),
        "albums": Album_home.objects.all(),
        "about_us": About_Us.objects.all(),
        "services": Services.objects.all(),
        "features": Features.objects.all(),
        'teams': Doctors.objects.all(),
        "testimonials": Testimonial.objects.all()

    }

    return render(request, "testimonial.html", data)


def signup(request):
    if request.POST:
        username = request.POST.get("username")

        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:

            return render(request, "signup.html", {"error": "Bunday akkaunt yaratilgan"})

        UserN = User.objects.create_user(username=username,  password=password, is_staff=True)
        UserN.save()

        return redirect("/login/")

    return render(request, "signup.html")
