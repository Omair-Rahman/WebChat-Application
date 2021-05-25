from django.shortcuts import render
from .models import displayUsername
from django.contrib.auth.models import User

# Create your views here.
def showUserName(request):
    displayNames = User.objects.all()
    return render (request, 'UserNameAll.html', {"displayUsername":displayNames})
