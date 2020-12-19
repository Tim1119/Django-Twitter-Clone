from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.views.generic import CreateView,UpdateView
from django.urls import reverse_lazy
from .forms import UserSignupForm,UserEditSettingsForm
from django.views.generic import DetailView 
from clone.models import Profile
from django.shortcuts import get_object_or_404
# Create your views here.

class SignupView(CreateView):
    form_class = UserSignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class EditUserSettingsView(UpdateView):
    form_class = UserEditSettingsForm
    template_name = 'registration/edit_settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
