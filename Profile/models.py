from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(default="NONE", max_length = 100)
    address = models.CharField(default="NONE", max_length = 100)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone_number = models.CharField(default="NONE", max_length = 20)
    profession = models.CharField(default="NONE", max_length = 100)
    linkedin_profile = models.CharField(default="#", max_length = 100)
    github_profile = models.CharField(default="#", max_length = 100)
    facebook_profile = models.CharField(default="#", max_length = 100)
    skils = models.CharField(default="NONE", max_length = 100)


    def __str__(self):
        return f'{self.user.username} Profile'
