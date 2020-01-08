from django.urls import path
from .views import Home_View_User

app_name = "User"

urlpatterns = [
    path('Home', Home_View_User, name="Home"),
]
