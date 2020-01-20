from django.urls import path
from .views import Home_View_Company, Register_view, Login_view, Logout_view,Add_profile_view , Add_new_password, Forgot_password, Otp_match, Show_profile_view, Edit_profile_view, Account_verification_view, Please_verify_view
app_name = "Company"

urlpatterns = [
    path('Home', Home_View_Company, name="Home"),
    path('Register', Register_view, name="Register"),
    path('Verify', Please_verify_view, name="Please_verify"),
    path('Verification', Account_verification_view, name="Verification"),
    path('Login', Login_view , name="Login"),
    path('Logout', Logout_view , name="Logout"),
    path('Profile',Show_profile_view,name="Show_profile"),
    path('Add_profile', Add_profile_view , name="Add_profile"),
    path('Edit_profile/<int:pk>', Edit_profile_view , name="Edit_profile"),
    path('Forgot_password', Forgot_password, name="Forgot_password" ),
    path('Add_new_password', Add_new_password, name="Add_New_Password" ),
    path('Enter_otp', Otp_match, name="Enter_otp" ),

]
