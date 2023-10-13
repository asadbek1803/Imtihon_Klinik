from django.db import models

# Create your models here.

class Statics(models.Model):
    expert_doctors = models.PositiveIntegerField()
    medical_stuff = models.PositiveIntegerField()
    patients = models.PositiveIntegerField()

    def __str__(self):
        return f"Experts: {self.expert_doctors}, Stuff: {self.medical_stuff}"

class Services(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    about = models.TextField()
    more = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Features(models.Model):
    icon = models.CharField(max_length=45)
    title = models.CharField(max_length=120)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.title

class Doctors(models.Model):
    image = models.ImageField(upload_to='doctors/images/')
    full_name = models.CharField(max_length=140)
    staff_name = models.CharField(max_length=140)

    # Social links

    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.full_name

class Appointment(models.Model):
    name = models.CharField(max_length=140)
    email = models.EmailField()
    phone = models.CharField(max_length=19)
    doctor = models.ForeignKey(Doctors, on_delete=models.Model)
    date = models.DateField(auto_now=False)
    datetime = models.DateTimeField(auto_now=False)
    about = models.TextField()


    def __str__(self):
        return f"Full name: {self.name}"

class Testimonial(models.Model):
    image = models.ImageField(upload_to='testimonials/images/')
    text = models.TextField()
    full_name = models.CharField(max_length=74)
    job = models.CharField(max_length=90)


    def __str__(self):
        return self.full_name

