from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'lgn.html')
def home(request):
    return render(request,'index.html')
def signup(request):
    return render(request,'registration/rig.html')