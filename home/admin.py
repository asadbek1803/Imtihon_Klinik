from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Statics
# Register your models here.

@admin.register(Statics)
class StaticsAdmin(ModelAdmin):
    list_display = ('expert_doctors', 'medical_stuff', 'patients')
    list_editable = ('medical_stuff', 'patients')
    list_filter = ('expert_doctors', 'medical_stuff', 'patients')