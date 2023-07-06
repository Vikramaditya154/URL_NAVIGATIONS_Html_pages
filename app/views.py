from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def registation(request):
    return render(request,'registation.html')

def login(request):
    return render(request,'login.html')