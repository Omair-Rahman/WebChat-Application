from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def login(request):
    context = {}
    if(request.method=='POST'):
        username = request.POST['username']
        password = request.POST['password']

    user = auth.authenticate(username=username,password=password)

    if(user is not None):
        auth.login(request,user)
        return redirect('dashboard')
    else:
        return render(request,'registration/login.html',context)

def signup(request):
    context = {}
    if(request.method=='POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if(password1==password2):
            if(User.objects.filter(username=username).exists()):
                messages.error(request,"Username already exist")
                return redirect('signup')
            elif(User.objects.filter(email=email).exists()):
                messages.error(request,"Email already exist")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                return redirect('home')
        else:
            messages.error(request,"Password does not match")
            return redirect('signup')
    else:
        return render(request,'registration/signup.html',context)
