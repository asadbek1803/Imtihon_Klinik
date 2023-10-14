from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Statics, Album_home, About_Us, Services, Features, Doctors, Appointment, Testimonial, Contact
# Register your models here.
admin.site.register(About_Us)

@admin.register(Statics)
class StaticsAdmin(ModelAdmin):
    list_display = ('expert_doctors', 'medical_stuff', 'patients')
    list_editable = ('medical_stuff', 'patients')
    list_filter = ('expert_doctors', 'medical_stuff', 'patients')

@admin.register(Album_home)
class Album(ModelAdmin):
    list_display = ('image_name', )

@admin.register(Services)
class ServicesAdmin(ModelAdmin):
    list_display = ('title', 'about', 'more')
    list_editable = ('about', 'more')
    list_filter = ('title', )
    search_fields = ('title', )

@admin.register(Features)
class FeaturesAdmin(ModelAdmin):
    list_display = ('title', 'name')
    list_editable = ('name', )
    search_fields = ('title', 'name')


@admin.register(Doctors)
class DoctorsAdmin(ModelAdmin):
    list_display = ('full_name', 'staff_name', 'facebook', 'twitter', 'instagram')
    list_editable = ('staff_name', 'facebook', 'twitter', 'instagram')
    search_fields = ('full_name', 'staff_name')


@admin.register(Appointment)
class AppointmentAdmin(ModelAdmin):
    list_display = ('name', 'email', 'phone', 'doctor', 'date', 'datetime', 'about')
    search_fields = ('name', 'phone', 'date', 'email')

@admin.register(Testimonial)
class TestersAdmin(ModelAdmin):
    list_display = ('full_name', 'job', 'text')
    list_editable = ('job', 'text')
    search_fields = ('full_name', 'job')

@admin.register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    search_fields = ('name', 'email')
