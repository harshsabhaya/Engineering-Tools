from django.urls import path
from .views import  Add_To_Wish_List_View
app_name = "Cart"

urlpatterns = [
    path('Add_To_Wishlist', Add_To_Wish_List_View, name="Add_To_WishList"),

]