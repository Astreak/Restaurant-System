from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *
from .forms import *

def home(req):
    J=Employee.objects.filter(account=req.user).first()
    I=Order.objects.filter(response=J)
    cnt=I.count()
    return render(req,"Order/home.html",{"H":cnt});
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
           
            
           
            form.save()
            return redirect("main-home");
    else:
        form=OrderForm()
    return render(req,"Order/Order.html",{"F":form})

class Getting_order(ListView):
    template_name="Order/show.html"
    def get_queryset(self):
        
        J=Employee.objects.filter(account=self.request.user).first()
        Q=Order.objects.filter(response=J)
        return Q;


class SHOW(ListView):
    template_name="Order/employee.html"
    def get_queryset(self):
        Q=Employee.objects.all()
        return Q;

class MyOrder(ListView):
    template_name="Order/MyOrder.html"
    def get_queryset(self):
        Q=Order.objects.filter(buyer=self.request.user)
        return Q;

def delivered(req,id):
    M={"PIZZA":123,"MACCARONI":334,"PASTA":90,"Burger":50,"Chicken":100}
    V=Order.objects.filter(id=id).first()
    R=V.response
    A=V.Choice
    bo=int(V.B)
    k=int(M[A])
   
    g=Employee.objects.filter(id=R.id).first()
    O=Monetary.objects.filter(user=g).first()
    O.Money+=k
    O.bonus=bo;
    O.save()
    Order.objects.filter(id=id).delete()
    return redirect('main-home')
def ACCOUNT(req):
    A=Employee.objects.filter(account=req.user).first()
    print(A)
    G=Monetary.objects.filter(user=A).first()
    return render(req,"Order/account.html",{"F":G})
