from django.urls import path
from .views import Home_View_User,My_Account_View, Update_Account_Info_View, All_Company_View, All_Product_By_Company, Product_Details_View

app_name = "User"

urlpatterns = [
    path('', Home_View_User, name="Home"),
    path('Account', My_Account_View, name="My_Account"),
    path('Update_Account', Update_Account_Info_View, name="Update_Account"),
    path('All_Company', All_Company_View, name="All_Company"),
    path('Products_By_Company', All_Product_By_Company, name="All_Product_By_Company"),
    path('Product_Details/<int:ID>', Product_Details_View, name="Product_Details"),
]
