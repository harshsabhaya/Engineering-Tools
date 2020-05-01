from django.shortcuts import render, redirect
from Company.models import Company_Profile, Product_Catagory
from django.contrib.auth.models import User


# Create your views here.
def ET_login(request):
    temp = "ET_Admin/login.html"
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print('\n')
        print(password)

        if username == "Admin" and password == "Admin":
            print("Admin Login Done")
            return redirect("Admin:Admin_home")
        else:
            print("Username and password not match, Login Fail")

    return render(request,temp)


def ET_Home(request):
    temp = "ET_Admin/index.html"
    return render(request,temp)

def ET_All_Company(request):
    temp = "ET_Admin/all_company.html"
    data = Company_Profile.objects.all()
    return render(request, temp, {'company':data})

def ET_Product_Category(request):
    temp = "ET_Admin/all_categories.html"
    data = Product_Catagory.objects.all()
    return render(request, temp, {'category':data})

def ET_All_User(request):
    temp = "ET_Admin/all_user.html"
    data = User.objects.all()
    return render(request, temp, {'user':data})

def ET_All_Feedback(request):
    temp = "ET_Admin/all_feedback.html"
    data = User.objects.all()
    return render(request, temp, {'user':data})
