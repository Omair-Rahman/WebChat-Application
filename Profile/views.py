from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models
from django.contrib import messages
from .forms import ProfileUpdateForm

# Create your views here.
@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def EditProfile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'form': form
    }
    return render(request, 'UpdateProfile.html', context)
