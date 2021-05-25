from django.urls import path
from home import views

urlpatterns = [
    path('',views.home,name="home"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('about/',views.about,name="about"),
]
