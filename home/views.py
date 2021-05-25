from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    context = {}
    return render(request,'index.html',context)

@login_required
def dashboard(request):
    context = {}
    return render(request,'dashboard.html',context)

def about(request):
    context = {}
    return render(request,'about.html',context)
