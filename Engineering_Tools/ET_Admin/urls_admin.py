from django.urls import path
from .views import ET_login, ET_Home, ET_All_Company, ET_Product_Category, ET_All_User
app_name = 'Admin'

urlpatterns = [
    path('',ET_login, name="Admin_login"),
    path('Home/', ET_Home, name="Admin_home"),
    path('Companies/', ET_All_Company, name="Admin_company"),
    path('Categories/', ET_Product_Category, name="Admin_category"),
    path('Users', ET_All_User, name="Admin_user"),
]