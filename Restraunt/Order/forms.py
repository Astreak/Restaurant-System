from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

class EmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields=["account"]
class MonetaryForm(ModelForm):
    class Meta:
        model=Monetary
        fields=["user","Money","bonus"]
class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields=["buyer","response","Choice","B"]

