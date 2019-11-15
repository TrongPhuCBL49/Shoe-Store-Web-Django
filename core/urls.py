from django.urls import path
from .views import Home

app_name = 'core'

urlpatterns = [
    path('home/', Home, name='home'),
]
