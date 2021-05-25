from django.urls import path
from Profile import views

urlpatterns = [
    path('', views.profile, name="profile"),
    path('edit/', views.EditProfile, name="EditProfile"),
]
