from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from .forms import LoginForm

class Login(LoginView):
  form_class = LoginForm
  template_name = 'accounts/login.html'

class Logout(LoginRequiredMixin, LogoutView):
  template_name = 'accounts/login.html'