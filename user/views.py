from django.shortcuts import render,HttpResponse

# Create your views here.

def Login(request):
    return render(request,"login.html")

def Signup(request):
    return render(request,"signup.html")


def Home(request):
    return render(request,"home.html")
