from django.urls import path
from .views import Home_View_User,My_Account_View, Update_Account_Info_View

app_name = "User"

urlpatterns = [
    path('', Home_View_User, name="Home"),
    path('Account', My_Account_View, name="My_Account"),
    path('Update_Account', Update_Account_Info_View, name="Update_Account"),
]
