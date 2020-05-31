from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
import random


from .models import Register, Company_Profile
from .forms import register_form, login_form, forgot_password_form, otp_match_form, add_new_password_form, add_profile_form, edit_profile_form, Add_Hardware_product_form, Add_Software_product_form


# Create your views here.
def Home_View_Company(request):
    temp ="Company/index.html"

    if request.session.get('company_register') == None:
        return redirect("Company:Login")

    return render(request, temp)


def Register_view(request):
    temp = "Company/register.html"
    if request.method == 'POST':
        r_form = register_form(request.POST or None, request.FILES or None)
        print("In form")
        if r_form.is_valid():
            print("form valid")
            register = r_form.save(commit = False)
            name = request.POST.get('c_name')
            email = request.POST.get('c_email')
            password = request.POST.get('c_password')
            c_password = request.POST.get('c_r_password')
            if (password == c_password):
                print("password match")
                register.save()
                request.session["company_email"] = email
                # email for welcome
                subject = "Sahil Rajput, Engineering Tools"
                message = "Hello, " + name + ". Welcome To Engineering Tools. Please Verify Your Email ID ::--> http://127.0.0.1:8000/Company/Verification"
                email_from = settings.EMAIL_HOST_USER
                email_to = [email, ]
                send_mail(subject, message, email_from, email_to)
                # email logic complate

                return redirect('Company:Please_verify')
    else:
        messages.error(request, 'Please Correct the error below.')
        r_form = register_form()

    return render(request, temp, {'register_form':r_form})


def Please_verify_view(request):
    temp = "Company/please_verify.html"
    return render(request,temp)


def Account_verification_view(request):
    temp = "Company/verification.html"
    return render(request,temp)


def Account_verification_done(request):
    email = request.session.get("company_email")
    Register.objects.filter(c_email=email).update(c_verification_flag=1)

    data = Register.objects.get(c_email=email)
    company = {'name': data.c_name, 'email': data.c_email}
    request.session["company_register"] = company

    if (data.c_verification_flag == True):
        return redirect('Company:Home')


def Login_view(request):
    temp = "Company/login.html"
    if request.method == 'POST':
        l_form = login_form(request.POST or None)
        if l_form.is_valid():
            email = request.POST.get('c_email')
            password = request.POST.get('c_password')
            print(email + " " + password)
            is_email = Register.objects.filter(c_email__iexact=email).exists()
            is_pass = Register.objects.filter(c_password__iexact=password).exists()
            print(is_email)
            print(is_pass)
            if is_email and is_pass:
                data = Register.objects.get(c_email=email)
                if (data.c_password == password):
                    print(data.c_password)
                    company = {'name': data.c_name, 'email': data.c_email}
                    request.session["company_register"] = company
                    return redirect('Company:Home')
    else:
        l_form = login_form()

    return render(request, temp, {'login_form':l_form})


def Logout_view(request):
    temp = "Company/logout.html"
    return render(request,temp,{})


def Logout_done(request):
    if (request.session.get("company_register") != None):
        request.session.delete()
        return redirect('Company:Login')
    else:
        return redirect('Company:Login')


def Forgot_password(request):
    temp = "Company/forgot_password.html"
    if request.method == 'POST':
        f_p_form = forgot_password_form(request.POST)
        if f_p_form.is_valid():
            email = request.POST.get('email')
            is_email = Register.objects.filter(c_email__iexact=email).exists()
            if is_email:
                OTP = random.randint(111111,999999)

                #email OTP send Logic
                subject = "Password Reset OTP @Engineering_Tools"
                message = "Your OTP is, " + str(OTP) + " .Please Follow This Link, --> http://127.0.0.1:8000/Company/Home"
                email_from = settings.EMAIL_HOST_USER
                email_to = [email,]
                send_mail(subject,message,email_from,email_to)
                #email OTP done

                #OTP and email set In Session
                request.session["reset_password_OTP"] = OTP
                request.session["reset_password_EMAIL"] = email
                return redirect('Company:Enter_otp')
    else:
        f_p_form = forgot_password_form()

    return render(request,temp, {'form':f_p_form})


def Otp_match(request):
    temp = "Company/enter_otp.html"
    if request.method == 'POST':
        e_otp_form = otp_match_form(request.POST)
        if e_otp_form.is_valid():
            otp = request.POST.get('otp')
            session_otp = request.session.get('reset_password_OTP')
            if str(otp) == str(session_otp):
                return redirect('Company:Add_New_Password')
    else:
        e_otp_form = otp_match_form()

    return render(request, temp, {'form':e_otp_form})


def Add_new_password(request):
    temp = "Company/Add_new_password.html"
    if request.method == 'POST':
        add_password_form = add_new_password_form(request.POST)
        if add_password_form.is_valid():
            passwd = request.POST.get('c_password')
            c_passwd = request.POST.get('c_r_password')
            if passwd == c_passwd:
                email = request.session.get('reset_password_EMAIL')
                Register.objects.filter(c_email = email).update(c_password = passwd, c_r_password = passwd)
                request.session.delete()
                return redirect('Company:Login')
    else:
        add_password_form = add_new_password_form()

    return render(request,temp, {'form':add_password_form})


def Add_profile_view(request):
    temp = "Company/add_profile.html"
    if request.method == 'POST':
        p_form = add_profile_form(request.POST or None, request.FILES or None)
        if p_form.is_valid():
            company = request.session.get("company_register")
            email = company["email"]
            name = company["name"]
            profile_form = p_form.save(commit = False)
            profile_form.c_email = email
            profile_form.c_name = name
            profile_form.save()
            company_details = Company_Profile.objects.get(c_email = email)
            request.session["company_id"] = company_details.id
            return redirect('Company:Home')
    else:
        p_form = add_profile_form()

    return render(request, temp, {'p_form':p_form})


def Show_profile_view(request):
    temp = "Company/profile.html"
    company = request.session.get("company_register")
    email = company['email']
    is_profile = Company_Profile.objects.filter(c_email__iexact=email).exists()
    print(is_profile)
    if is_profile:
        data = Company_Profile.objects.get(c_email = email)
    return render(request,temp, {'data':data})


def Edit_profile_view(request, pk):
    temp = "Company/edit_profile.html"
    profile = get_object_or_404(Company_Profile,pk=pk)
    form = edit_profile_form(request.POST or None, request.FILES or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect("Company:Show_profile")
    return render(request,temp, {'p_form':form})


def Product_Hardware_view(request):
    temp = "Company/Add_Hardware_product.html"
    if request.method == 'POST':
        print("form post")
        hardware_form = Add_Hardware_product_form(request.POST or None, request.FILES or None)
        print(request.POST.get("p_name"))
        print(request.POST.get("p_company_id"))
        print(request.POST.get("p_manufacturing_date"))
        print(request.POST.get("p_catagory"))
        if hardware_form.is_valid():
            print("is valid")
            hardware_product_form = hardware_form.save(commit=False)
            #hardware_product_form.p_company_id = 2 # this value needs to be dynamic

            hardware_product_form.save()
            print("form save")
            return redirect("Company:Home") #needs to redirect at show hardware product page
        else:
            print("Form not valid")
    else:
        hardware_form = Add_Hardware_product_form()

    return render(request, temp, {"product_hardware_form":hardware_form})


def Product_Software_view(request):
    temp = "Company/Add_Software_product.html"

    if request.method == "POST":
        software_form = Add_Software_product_form(request.POST or None, request.FILES or None)
        if software_form.is_valid():
            software_product_form = software_form.save(commit = False)
            software_product_form.save()
            return redirect("Company:Home")
        else:
            print("Form Not Valid")
    else:
        software_form = Add_Software_product_form()
    return render(request, temp, {"product_software_form":software_form})



def All_Hardware_product_view(request):
    temp = "Company/all_hardware.html"
    return render(request,temp)

def All_Software_product_view(request):
    temp = "Company/all_software.html"
    return render(request, temp)