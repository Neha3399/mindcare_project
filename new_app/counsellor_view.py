from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from new_app.forms import CounsilerRegister, Fdbk_c
from new_app.models import Request, Counsiler, feedback_c

@login_required(login_url='login_view')
def counsiler_base(request):
    return render(request,"Counsiler/Counsiler_base.html")


@login_required(login_url='login_view')
def req_donor(request,):
    data=Request.objects.all()
    return render(request, "Counsiler/request_view.html", {'data':data})


@login_required(login_url='login_view')
def Donate(request,id):
    obj=Request.objects.get(id=id)
    user1 = request.user
    data =  Counsiler.objects.get(user=user1)
    obj.CounsilerName=data

    obj.Status = 1
    obj.save()
    return redirect("view_request")


@login_required(login_url='login_view')
def feedbk_c(request):
    data = Fdbk_c()
    user1 = request.user
    rcvr = Counsiler.objects.get(user=user1)


    if request.method == "POST":
        Req = Fdbk_c(request.POST)
        if Req.is_valid():
            obj = Req.save(commit=False)
            obj.name = rcvr
            obj.save()

    return render(request,"Counsiler/feedback.html",{"data":data})


@login_required(login_url='login_view')
def replay_c(request):
    user1 = request.user
    data = Counsiler.objects.get(user=user1)
    obj = feedback_c.objects.filter(name=data)
    return render(request,"Counsiler/replay_c.html",{"data":obj})


@login_required(login_url='login_view')
def profile_counsiler(request):
    user1= request.user
    data=Counsiler.objects.get(user=user1)
    return render (request,'Counsiler/profile.html',{'form':data})


@login_required(login_url='login_view')
def profile_update(request,id):
    data=Counsiler.objects.get(id=id)
    form= CounsilerRegister(instance=data)
    if request.method == "POST":
        profile=CounsilerRegister(request.POST,request.FILES,instance=data)
        if profile.is_valid():
           profile.save()
        return redirect("profile_counsiler")
    return render(request,"Counsiler/profile_update.html",{"form":form})

def logou(request):
    logout(request)
    return redirect("/")