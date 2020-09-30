from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    account=models.OneToOneField(User,default=1,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.account.username}"

class Monetary(models.Model):
    user=models.OneToOneField(Employee,default=1,on_delete=models.CASCADE)
    Money=models.IntegerField(default=0);
    bonus=models.IntegerField(default=0);
    def __str__(self):
        return f"{self.user.account.username}'s Account";

class Order(models.Model):
    M={"PIZZA":123,"MACCARONI":334,"PASTA":90,"Burger":50,"Chicken":100}
    C=[("PIZZA","PZ"),
       ("MACCARONI","MCC"),
       ("PASTA","PST"),
       ("Burger","BG"),
       ("Chicken","CHK")]
    buyer=models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    response=models.ForeignKey(Employee,default=1,on_delete=models.CASCADE)
    Choice=models.CharField(choices=C,max_length=100,default="PIZZA")
    F=models.IntegerField(default=0)
    B=models.IntegerField(default=0)
    def __str__(self):
        return f"{self.Choice} to {self.response}";