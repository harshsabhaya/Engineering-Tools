from django.urls import path
from .views import Home_View_Company, Register_view, Login_view, Logout_view, Profile_view
app_name = "Company"

urlpatterns = [
    path('Home', Home_View_Company, name="Home"),
    path('Register', Register_view, name="Register"),
    path('Login', Login_view , name="Login"),
    path('Logout', Logout_view , name="Logout"),
    path('Profile', Profile_view , name="Profile"),
]
