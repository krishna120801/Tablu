from django.shortcuts import redirect, render
from django.http import *
from tablecreation.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
import base64,os
from PIL import Image
from io import BytesIO
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.contrib.auth.models import User
def signin(request):
    logout(request)
    emai = passs = ''
    if request.method=='POST':
        emai = request.POST['email']
        passs = request.POST['password']
        try:
            m=User.objects.get(email=emai)
            user = authenticate(username=m, password=passs)
        except:
            messages.error(request, "Invalid Email or Password.")
            return render(request,'registration/login.html')
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
@login_required(login_url="login")
def main(request):
    data=request.GET.get('data')
    name=str(request.user.username)
    str1='folders/'+name+ "_userhis.pdf"
    if data!=None:
        data=data.replace("data:image/png;base64","")
        im = Image.open(BytesIO(base64.b64decode(data)))
        if im.mode=="RGBA":
            im=im.convert("RGB")
        im.save(str1, 'PDF')
    return render(request,'fsttblpg.html',{'user':request.user.username})
def showpdf(request):
    name=str(request.user.username)
    str1=name+"_userhis.pdf"
    filepath = os.path.join('folders',str1 )
    try:
        return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
    except:
        msg="I think You hadn't create any table before please create a table"
        return HttpResponse('<small style="padding: 0!important;"class="text-center alert alert-warning ">'+msg+'</small><h1>Please Go back to previous page</h1>')
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
            user = authenticate(username=username, password=password1)
            login(request, user)
            return redirect('tablu')
    return render(request, 'registration/rig.html')  