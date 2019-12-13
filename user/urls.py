from django.urls import path
from .views import RegisterView

app_name = 'product'

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
]
