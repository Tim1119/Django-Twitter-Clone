from django.urls import path,include
from .views import SignupView,EditUserSettingsView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',SignupView.as_view(),name='signup'),
    path('login/',SignupView.as_view(),name='login'),
    path('edit_settings/',EditUserSettingsView.as_view(),name='edit_settings'),
    path('password/',auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'),name="change-password"),
  
    
]
