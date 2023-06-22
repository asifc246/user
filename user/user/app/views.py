from django.shortcuts import render,redirect
from app.models import Login,user

# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        return redirect('')
    else:
        return render(request,'login.html')
    
def register(request):
    if request.method=='POST':
        name=request.POST['name']
        gender=request.POST['gender']
        email=request.POST['email']
        uobj=user()
        uobj.name=name
        uobj.gender=gender
        uobj.email=email
        uobj.save()
        return redirect('/verification/')
    else:
        return render(request,'register.html')

def verification(request):
    if request.method=='POST':
        otp=request.POST['otp']
        return redirect('')
    else:
        return render(request,'verification.html')