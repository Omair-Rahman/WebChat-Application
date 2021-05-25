from django.urls import path
from . import views

urlpatterns = [
    path("", views.showUserName, name="user-name"),
]
