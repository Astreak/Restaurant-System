from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def home(req):
    return render(req,"Order/home.html");
def info(req):
    return HttpResponse("Hey there Work on progress");

def register(req):
    if req.method=="POST":
        form=RegisterForm(req.POST)
        if form.is_valid():
            form.save();
            return redirect("main-home")
    else:
        form =RegisterForm()
    return render(req,"Order/register.html",{"F":form})

def employee(req):
    if req.method=="POST":
        form=EmployeeForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("main-Money");
    else:
        form=EmployeeForm()
    return render(req,"Order/Emp.html",{"F":form})

def monetary(req):
    if req.method=="POST":
            form=MonetaryForm(req.POST)
            if form.is_valid():
                form.save()
                return redirect("main-home");
    else:
        form=MonetaryForm()
    return render(req,"Order/mon.html",{"F":form})

def order(req):
    if req.method=="POST":
        form=OrderForm(req.POST)
        J=req.POST.get("buyer")
        
        R=req.POST.get("response")
        if form.is_valid() and J!=R:
            M={"PIZZA":123,"MACCARONI":334,"PASTA":90,"Burger":50,"Chicken":100}
            A=req.POST.get("Choice")
            bo=int(req.POST.get("B"))
            k=int(M[A])
            print(k)
            g=Employee.objects.filter(id=R).first()
            O=Monetary.objects.filter(user=g).first()
            O.Money+=(k+bo)
            O.save()
            
           
            form.save()
            return redirect("main-home");
    else:
        form=OrderForm()
    return render(req,"Order/Order.html",{"F":form})

