from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

urlpatterns = [
    path('register/', CreateView.as_view(
        template_name='users/register.html',
        form_class=CustomUserCreationForm,
        success_url=reverse_lazy('login')
    ), name='register'),

    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        next_page='login'
    ), name='logout'),
]
