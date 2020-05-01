from django.urls import path
from .views import ET_login, ET_Home
app_name = 'Admin'

urlpatterns = [
    path('',ET_login, name="Admin_login"),
    path('Home/', ET_Home, name="Admin_home"),
]