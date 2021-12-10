from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('Signup/',views.RegistrationAPIView.as_view(),name='Register'),
    path('login/',views.LoginAPIView.as_view(),name='Login')

]