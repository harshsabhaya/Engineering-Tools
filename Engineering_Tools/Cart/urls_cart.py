from django.urls import path
from .views import  Add_To_Wish_List_View, Remove_From_Wish_List_View
app_name = "Cart"

urlpatterns = [
    path('Add_To_Wishlist', Add_To_Wish_List_View, name="Add_To_WishList"),
    path('Remove_From_Wishlist', Remove_From_Wish_List_View, name="Remove_From_WishList"),

]