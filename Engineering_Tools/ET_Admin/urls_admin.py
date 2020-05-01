from django.urls import path
from .views import ET_login
app_name = 'Admin'

urlpatterns = [
    path('',ET_login, name="Admin_login"),
]