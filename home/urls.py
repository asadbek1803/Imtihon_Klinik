from django.urls import path
from .views import home, service, about, signup, team, contact, logout_u, testimonial, appointment, feature, Error404, login_u

urlpatterns = [
    path("", home, name='home'),
    path("service/", service, name='service'),
    path("about/", about, name='about'),
    path("team/", team, name='team'),
    path("contact/", contact, name='contact'),
    path("testimonial/", testimonial, name='testimonial'),
    path("appointment/", appointment, name='appointment'),
    path("feature/", feature, name='feature'),
    path("404/", Error404, name='404'),
    path("login/", login_u, name='login'),
    path("logout/", logout_u, name="logout"),
    path("signup/", signup, name="signup")

]