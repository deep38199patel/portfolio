from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
     path('', views.IndexView.as_view(), name='index'),
     path('profile', views.ProfileView.as_view(), name='profile'),
     path('signup', views.SignUpView.as_view(), name='signup'),
     path('login', views.LogInView.as_view(), name='login'),
]