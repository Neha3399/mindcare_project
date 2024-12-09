from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from new_app.forms import LoginRegister, CounsilerRegister, PatientRegister


# Create your views here.
def demo(request):
    return render(request,"test.html")

def land(request):
    return render(request,"index.html")


def dash(request):
    return render(request,"index1.html")

def Log(request):
    return render(request,"Login.html")

def CounsilerR(request):
    form1 = LoginRegister()
    form2=CounsilerRegister()

    if request.method =="POST":
               form1 = LoginRegister(request.POST)
               form2 = CounsilerRegister(request.POST,request.FILES)

               if form1.is_valid() and form2.is_valid():
                   user1=form1.save(commit=False)
                   user1.is_Counsiler=True
                   user1.save()
                   user2=form2.save(commit=False)
                   user2.user=user1
                   user2.save()
                   return redirect('login_view')
    return render(request,"Counsilerregister.html",{"form1":form1,"form2":form2} )

def PatientR(request):
    form1 = LoginRegister()
    form2= PatientRegister()

    if request.method =="POST":
               form1 = LoginRegister(request.POST)
               form2 = PatientRegister(request.POST,request.FILES)

               if form1.is_valid() and form2.is_valid():
                   user1=form1.save(commit=False)
                   user1.is_patient=True
                   user1.save()
                   user2=form2.save(commit=False)
                   user2.user=user1
                   user2.save()
                   return redirect('login_view')
    return render(request,"patient_register.html",{"form1":form1,"form2":form2} )


def login_view(request):
    if request.method == 'POST':
        username= request.POST.get('uname')
        password= request.POST.get('password')
        print(username)
        print(password)
        user= authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            print("ok")
            if user.is_staff:
                print("admin")
                return redirect('admin_base')
            elif user.is_Counsiler:
                print("admin")
                return redirect('counsiler_base')
            elif user.is_patient:
                print("admin")
                return redirect('patient_base')
        else:
            messages.info(request,"Invalid credentials")
    return render(request,"Login.html")