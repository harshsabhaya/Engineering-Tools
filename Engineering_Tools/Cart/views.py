from django.shortcuts import render, redirect, reverse
from Company.models import Product_Hardware
from . models import Wishlist, Cart
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
        return redirect(reverse('User:Product_Details', args=(P_ID,)))
    else:
        return redirect("User:Home")


def Remove_From_Wish_List_View(request):
    if request.method == "POST":
        P_ID = request.POST.get("productId")
        Wishlist.objects.get(product= P_ID, user=request.user).delete()
        return redirect(reverse('User:Product_Details', args=(P_ID,)))
    else:
        return redirect("User:Home")



def Add_To_Wish_List_From_All_product_View(request):
    if request.method == "POST":
        product_name = request.POST.get("productName")
        user_name = request.user.username
        user_email = request.user.email
        price = request.POST.get("productPrice")
        P_ID = request.POST.get("productId")
        product = Product_Hardware.objects.get(id = P_ID)
        user = request.user
        Wishlist.objects.create(product_name=product_name, user_name=user_name, user_email=user_email, price=price, product_id=product.id, user_id=user.id)
        return redirect('User:Wishlist')
    else:
        return redirect("User:Home")


def Remove_From_Wish_List_From_All_Product_View(request):
    if request.method == "POST":
        P_ID = request.POST.get("productId")
        Wishlist.objects.get(product= P_ID, user=request.user).delete()
        return redirect('User:Wishlist')
    else:
        return redirect("User:Home")


def Remove_From_WishList_View(request):
    if request.method == "POST":
        ID = request.POST.get("ID")
        Wishlist.objects.get(id=ID, user=request.user).delete()
        return redirect('User:Wishlist')
    else:
        return redirect("User:Home")


def Add_To_Cart_From_Details_View(request):
    if request.method == "POST":
        product_name = request.POST.get("productName")
        user_name = request.user.username
        user_email = request.user.email
        price = request.POST.get("productPrice")
        P_ID = request.POST.get("productId")
        product = Product_Hardware.objects.get(id=P_ID)
        user = request.user
        Cart.objects.create(product_name=product_name, user_name=user_name, user_email=user_email, price=price,product_id=product.id, user_id=user.id, quantity=1, sub_total=price)
        return redirect(reverse('User:Product_Details', args=(P_ID,)))
    else:
        return redirect("User:Home")



def Remove_From_Cart_From_Details_View(request):
    if request.method == "POST":
        P_ID = request.POST.get("productId")
        Cart.objects.get(product= P_ID, user=request.user).delete()
        return redirect(reverse('User:Product_Details', args=(P_ID,)))
    else:
        return redirect("User:Home")


def Add_To_Cart_From_All_Product_View(request):
    if request.method == "POST":
        product_name = request.POST.get("productName")
        user_name = request.user.username
        user_email = request.user.email
        price = request.POST.get("productPrice")
        P_ID = request.POST.get("productId")
        product = Product_Hardware.objects.get(id=P_ID)
        user = request.user
        Cart.objects.create(product_name=product_name, user_name=user_name, user_email=user_email, price=price,product_id=product.id, user_id=user.id, quantity=1, sub_total=price)
        return redirect('User:Cart')
    else:
        return redirect("User:Home")

def Remove_From_Cart_From_All_Product_View(request):
    if request.method == "POST":
        P_ID = request.POST.get("productId")
        Cart.objects.get(product= P_ID, user=request.user).delete()
        return redirect('User:Cart')
    else:
        return redirect("User:Home")
