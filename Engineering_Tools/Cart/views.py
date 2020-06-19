from django.shortcuts import render, redirect
from Company.models import Product_Hardware
from . models import Wishlist
# Create your views here.
def Add_To_Wish_List_View(request):
    if request.method == "POST":
        product_name = request.POST.get("productName")
        user_name = request.user.username
        user_email = request.user.email
        price = request.POST.get("productPrice")
        P_ID = request.POST.get("productId")
        product = Product_Hardware.objects.get(id = P_ID)
        user = request.user
        Wishlist.objects.create(product_name=product_name, user_name=user_name, user_email=user_email, price=price, product_id=product.id, user_id=user.id)
        return redirect("User:Wishlist")
    else:
        return redirect("User:Home")