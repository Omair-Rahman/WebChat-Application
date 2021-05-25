from django import forms
from django.contrib.auth.models import User
from .models import Profile


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'full_name', 'address', 'phone_number', 'profession', 'linkedin_profile', 'github_profile', 'facebook_profile', 'skils']
