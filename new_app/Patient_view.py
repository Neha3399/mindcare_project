from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from new_app.forms import p_request, Fdbk, PatientRegister
from new_app.models import Patient, Request, feedback

@login_required(login_url='login_view')
def patient_base(request):
    return render(request,"Patient/Patient_base.html")


@login_required(login_url='login_view')
def req(request):
    data=p_request()
    user1=request.user
    print(user1)
    rcvr=Patient.objects.get(user=user1)
    print(rcvr)

    if request.method == "POST":
        print("ok1")
        Req=p_request(request.POST)
        if Req.is_valid():
            print("ok2")
            obj = Req.save(commit=False)
            obj.PatientName = rcvr
            print("ok3")
            obj.save()
            print("ok4")
    return render(request,"Patient/request.html",{"form":data})

@login_required(login_url='login_view')
def req_table(request):
    user1=request.user
    data=Patient.objects.get(user=user1)
    obj= Request.objects.filter(PatientName=data)
    return render(request, "Patient/request_view.html",{'data':obj} )


@login_required(login_url='login_view')
def rmv_req(request,id):
    data=Request.objects.get(id=id)
    data.delete()
    return redirect('request_view')


@login_required(login_url='login_view')
def feedbk(request):
    data = Fdbk()
    user1 = request.user
    rcvr = Patient.objects.get(user=user1)


    if request.method == "POST":
        Req = Fdbk(request.POST)
        if Req.is_valid():
            obj = Req.save(commit=False)
            obj.name = rcvr
            obj.save()

    return render(request,"Patient/feedback.html",{"data":data})

@login_required(login_url='login_view')
def replay(request):
    user1 = request.user
    data = Patient.objects.get(user=user1)
    obj = feedback.objects.filter(name=data)
    return render(request,"Patient/replay.html",{"data":obj})


@login_required(login_url='login_view')
def profile_patient(request):
    user1= request.user
    data=Patient.objects.get(user=user1)
    return render (request,'Patient/profile.html',{'form':data})


@login_required(login_url='login_view')
def patient_update(request,id):
    data=Patient.objects.get(id=id)
    form=  PatientRegister(instance=data)
    if request.method == "POST":
        profile= PatientRegister(request.POST,request.FILES,instance=data)
        if profile.is_valid():
           profile.save()
        return redirect("profile_patient")
    return render(request,"Patient/profile_update.html",{"form":form})

def logou(request):
    logout(request)
    return redirect("/")