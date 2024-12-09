from django import forms
from django.contrib.auth.forms import UserCreationForm

from new_app.models import Login, Counsiler, Patient, Request, feedback, feedback_c


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password = forms.CharField(label="passord", widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password')

class  CounsilerRegister(forms.ModelForm):
    class Meta:
        model= Counsiler
        fields ="__all__"
        exclude =("user",)

class  PatientRegister(forms.ModelForm):
    class Meta:
        model= Patient
        fields ="__all__"
        exclude =("user",)

class  p_request(forms.ModelForm):

    class Meta:
        model= Request
        fields ="__all__"
        exclude = ("PatientName","Status","CounsilerName",)


class Fdbk(forms.ModelForm):
    class Meta:
        model = feedback
        fields ="__all__"
        exclude = ("date","replay","name",)

class Fdbk_c(forms.ModelForm):
    class Meta:
        model = feedback_c
        fields ="__all__"
        exclude = ("date","replay","name",)