from django.shortcuts import render, redirect, reverse
from .models import Profile
from Company.models import Company_Profile, Product_Hardware, Register, Product_Catagory
from Company.forms import Product_Review_form
# Create your views here.

def Home_View_User(request):
    temp = "User/index.html"
    return render(request, temp)

def My_Account_View(request):
    temp = "User/my_account.html"
    ID = request.user.id
    data = Profile.objects.get(user_id = ID)
    print(data.gender)
    return render(request, temp, {'data':data})


def Update_Account_Info_View(request):
    if request.method == 'POST':
        number = request.POST.get("PhoneNumber")
        Gender = request.POST.get("genderSelect")
        Address = request.POST.get("address")
        City = request.POST.get("city")
        State = request.POST.get("state")
        Country = request.POST.get("country")
        Pincode = request.POST.get("pincode")
        ID = request.user.id
        Profile.objects.filter(user_id=ID).update(phone=number, gender=Gender, address_line=Address, city=City, state=State, country=Country, pincode=Pincode)
        return redirect('User:Home')
    else:
        return redirect('User:My_Account')


def All_Company_View(request):
    temp = "User/all_company.html"
    data = Company_Profile.objects.all()
    return render(request, temp, {'data':data})

def All_Product_By_Company(request):
    temp = "User/all_product_by_company.html"
    companyEmail = request.POST.get("Company_Email")
    company = Register.objects.get(c_email = companyEmail)
    data = Product_Hardware.objects.filter(p_company_id = company.id)
    return render(request, temp, {'data':data, 'CompanyName':company.c_name})

def Product_Details_View(request, ID):
    temp = "User/product_details.html"
    data = Product_Hardware.objects.get(id = ID)
    category = Product_Catagory.objects.get(id = data.p_catagory_id)
    review_form = Product_Review_form()
    return render(request, temp, {'data':data, 'categoryName':category.catagory_name, 'review_form':review_form})

def Add_Product_Review_View(request):
    temp = "User/product_details.html"
    product_id = request.POST.get('product_id')
    product_name = request.POST.get('product_name')
    if request.method == "POST":
        print("In post form")
        review_form = Product_Review_form(request.POST or None)
        print("form get")
        product = Product_Hardware.objects.get(id = product_id)
        user_id = request.user
        user_name = request.user.username
        user_email = request.user.email
        if review_form.is_valid():
            print("form Valid")
            form = review_form.save(commit=False)
            form.product = product
            form.product_name = product_name
            form.user = user_id
            form.user_name = user_name
            form.user_email = user_email
            review_form.save()
            return redirect(reverse('User:Product_Details', args=(product_id,)))
        else:
            print("form not valid")
    else:
        print("get")
        return redirect('User:All_Company')

