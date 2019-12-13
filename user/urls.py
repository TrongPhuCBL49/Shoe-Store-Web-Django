from django.urls import path
from .views import RegisterView, LoginView

app_name = 'user'

urlpatterns = [
    path('register/', RegisterView, name='register'),
    path('login/', LoginView, name='login'),
]
