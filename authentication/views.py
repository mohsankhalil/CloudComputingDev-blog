from django.shortcuts import render, redirect
from .form import UserCreateFm,UserLoginFm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def LoginView(request):
    if request.user.is_authenticated and not request.user.is_staff:
        return redirect("home")

    fm = UserLoginFm(request=request)
    if request.method == "POST":
         fm = UserLoginFm(request=request,data=request.POST)
         if fm.is_valid():
             username = fm.cleaned_data['username']
             pwd = fm.cleaned_data['password']
             user = authenticate(username=username,password=pwd)
             if user is not None:
                 login(request,user)
                 return redirect("home")
    return render(request,'auth/login.html',{'form':fm})

def RegistrationView(request):
    if request.user.is_authenticated and not request.user.is_staff:
        return redirect("home")
    
    fm = UserCreateFm()
    if request.method == "POST":
        fm = UserCreateFm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("login")
    return render(request,'auth/sign-up.html',{'form':fm})


def LogoutView(request):
    logout(request)
    return redirect("home")

