from django.shortcuts import redirect, render
from django.http import *
from tablecreation.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.contrib.auth.models import User
def signin(request):
    logout(request)
    emai = passs = ''
    if request.method=='POST':
        emai = request.POST['email']
        passs = request.POST['password']
        m=User.objects.get(email=emai)
        user = authenticate(username=m, password=passs)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('tablu')
        else:
            messages.error(request, "Invalid Email or Password.")
            return render(request,'registration/login.html')
    return render(request,'registration/login.html')
def home(request):
    return render(request,'index.html')
def main(request):
    return render(request,'fsttblpg.html')
def signup(request):
    if request.method == 'POST':   
            username = request.POST['name'].lower()  
            new = User.objects.filter(username = username)  
            if new.count():  
                messages.error(request, "User Already Exist")
                return render(request, 'registration/rig.html',)     
            email = request.POST['email'].lower()  
            new = User.objects.filter(email=email)  
            if new.count():  
                messages.error(request, " Email Already Exist")
                return render(request, 'registration/rig.html',)  
            password1 = request.POST['password1']  
            password2 = request.POST['password2']  
            if password1 and password2 and password1 != password2:  
                messages.error(request, "Password don't match")
                return render(request, 'registration/rig.html',)  
            user = User.objects.create_user(  
            username,
            email,
            password1)
            return redirect('tablu')
    return render(request, 'registration/rig.html')  