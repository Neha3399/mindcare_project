from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import DO_NOTHING


# Create your models here.
class Login(AbstractUser):
    is_Counsiler=models.BooleanField(default=False)
    is_patient=models.BooleanField(default=False)

class Counsiler(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name="Counsiler")
    Name=models.CharField(max_length=20)
    Age=models.CharField(max_length=3)
    Professional_title=models.CharField(max_length=10)
    License_number =models.CharField(max_length=10)
    Speciality=models.CharField(max_length=20)
    Year_of_experience=models.CharField(max_length=20)
    Education=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    Professional_membership=models.CharField(max_length=20)
    Session_length = (
        ('30min', '30min'),
        ('45min', '45min'),
        ('60min', '60min'),


    )
    Session = models.CharField(max_length=10, choices=Session_length)
    Session_frequency=(
        ('weekly','weekly'),
        ('biweekly','biweekly'),
    )
    frequency=models.CharField(max_length=20,choices=Session_frequency)
    document = models.FileField(upload_to='documents/')



class Patient(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name="Patient")
    Name = models.CharField(max_length=20)
    Age = models.CharField(max_length=3)
    Gender=models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    Merital_status=models.CharField(max_length=30)
    occupation=models.CharField(max_length=30)
    Reason_for_seeking_counsiling=models.CharField(max_length=50)
    Preferred_counsiling_approch=models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    document = models.FileField(upload_to='documents/')

class Request(models.Model):
    PatientName = models.ForeignKey('Patient', on_delete=models.CASCADE)
    CounsilerName = models.ForeignKey('Counsiler', on_delete=DO_NOTHING, blank=True, null=True)
    Age = models.CharField(max_length=3)
    Gender = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    Reason_for_seeking_counsiling = models.CharField(max_length=50)
    Preferred_counsiling_approch = models.CharField(max_length=30)
    Status = models.IntegerField(default=0)

class feedback(models.Model):
    name=models.ForeignKey("Patient",on_delete=models.CASCADE)
    massage=models.TextField()
    date=models.DateField(auto_now=True)
    replay=models.CharField(max_length=200,null=True,blank=True)

class feedback_c(models.Model):
    name=models.ForeignKey("Counsiler",on_delete=models.CASCADE)
    massage=models.TextField()
    date=models.DateField(auto_now=True)
    replay=models.CharField(max_length=200,null=True,blank=True)





