from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from new_app.forms import CounsilerRegister, PatientRegister
from new_app.models import Counsiler, Patient, Request, feedback, feedback_c

@login_required(login_url='login_view')
def admin_base(request):
    return render(request,"Admin/Admin_base.html")


@login_required(login_url='login_view')
def table_view(request):
    data=Counsiler.objects.all()
    return render(request, "admin/counsiler_view.html",{'data':data} )


@login_required(login_url='login_view')
def remove(request,id):
    data = Counsiler.objects.get(id=id)
    data.delete()
    return redirect("counsiler_view")


@login_required(login_url='login_view')
def update(request,id):
    data= Counsiler.objects.get(id=id)
    form= CounsilerRegister(instance=data)
    if request.method == "POST":
        session=CounsilerRegister(request.POST,instance=data)
        if session.is_valid():
           session.save()
           return redirect("counsiler_view")
    return render(request,"admin/update.html",{"form":form})


@login_required(login_url='login_view')
def table2_view(request):
    data=Patient.objects.all()
    return render(request, "admin/patient_view.html",{'data':data} )


@login_required(login_url='login_view')
def remove2(request,id):
    data = Patient.objects.get(id=id)
    data.delete()
    return redirect("patient_view")


@login_required(login_url='login_view')
def update2(request,id):
    data= Patient.objects.get(id=id)
    form= PatientRegister(instance=data)
    if request.method == "POST":
        Blo=PatientRegister(request.POST,instance=data)
        if Blo.is_valid():
           Blo.save()
           return redirect("patient_view")
    return render(request,"admin/update2.html",{"form":form})


@login_required(login_url='login_view')
def request_accept(request):
    obj = Request.objects.filter(Status=1)
    return render(request,"admin/request_accept.html",{'data':obj})

@login_required(login_url='login_view')
def accept(request,id):
    obj =Request.objects.get(id=id)
    obj.Status = 2
    obj.save()
    return redirect('request_accept')

@login_required(login_url='login_view')
def reject(request,id):
    obj=Request.objects.get(id=id)
    obj.Status = 0
    obj.save()
    return redirect('request_accept')


@login_required(login_url='login_view')
def accept_view(request):
    data = Request.objects.filter(Status=2)
    return render(request,"admin/accept_view.html",{"data":data})


@login_required(login_url='login_view')
def feedback_view(request):
    data = feedback.objects.all()
    return render(request,"admin/feedback_view.html",{"data":data})



@login_required(login_url='login_view')
def replay_feedback(request,id):
    Feedbak=feedback.objects.get(id=id)
    if request.method == "POST":
        r = request.POST.get('replay')
        Feedbak.replay = r
        Feedbak.save()

        # messages.info(request,"replay send ")
        return redirect('feedback_view')
    return render(request,"admin/replay_feedback.html",{'Feedbak':Feedbak})



@login_required(login_url='login_view')
def feedback_view_c(request):
    data = feedback_c.objects.all()
    return render(request,"admin/feedback_view_c.html",{"data":data})



@login_required(login_url='login_view')
def replay_feedback_c(request,id):
    Feedbak=feedback_c.objects.get(id=id)
    if request.method == "POST":
        r = request.POST.get('replay')
        Feedbak.replay = r
        Feedbak.save()

        # messages.info(request,"replay send ")
        return redirect('feedback_view_c')
    return render(request,"admin/replay_feedback_c.html",{'Feedbak':Feedbak})

def logou(request):
    logout(request)
    return redirect("/")