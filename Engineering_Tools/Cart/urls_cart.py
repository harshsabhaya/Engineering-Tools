from django.urls import path
from .views import  Add_To_Wish_List_View, Remove_From_Wish_List_View, Add_To_Wish_List_From_All_product_View,  Remove_From_Wish_List_From_All_Product_View, Remove_From_WishList_View, Add_To_Cart_From_Details_View, Remove_From_Cart_From_Details_View, Add_To_Cart_From_All_Product_View
app_name = "Cart"

urlpatterns = [
    path('Add_To_Wishlist', Add_To_Wish_List_View, name="Add_To_WishList"),
    path('Remove_From_Wishlist', Remove_From_Wish_List_View, name="Remove_From_WishList"),
    path('Add_To_Wishlist_From_All_Product', Add_To_Wish_List_From_All_product_View, name="Add_To_WishList_From_All_Product"),
    path('Remove_From_WishList_From_All_Product', Remove_From_Wish_List_From_All_Product_View, name="Remove_From_WishList_From_All_Product"),
    path('Remove_From_WishList', Remove_From_WishList_View, name="Remove_From_Wish_LIST"),
    path('Add_To_Cart', Add_To_Cart_From_Details_View, name="Add_To_Cart"),
    path('Remove_From_Cart', Remove_From_Cart_From_Details_View, name="Remove_From_Cart"),
    path('Add_To_Cart_From_All_Product', Add_To_Cart_From_All_Product_View, name="Add_To_Cart_From_All_Product_View"),
]