from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
import random


from .models import Register, Company_Profile
from .forms import register_form, login_form, forgot_password_form, otp_match_form, add_new_password_form, edit_profile_form


# Create your views here.
def Home_View_Company(request):
    temp ="Company/index.html"

    email = request.session.get('company_details')
    if email == None:
        return redirect("Company:Login")

    return render(request, temp)



def Register_view(request):
    temp = "Company/register.html"
    if request.method == 'POST':
        r_form = register_form(request.POST or None, request.FILES or None)
        if r_form.is_valid():
            register = r_form.save(commit = False)
            password = request.POST.get('c_password')
            c_password = request.POST.get('c_r_password')
            if (password == c_password):
                register.save()
                data = Register.objects.get(c_email=request.POST.get('c_email'))
                request.session["company_details"] = data.c_email
                request.session["company_name"] = data.c_name
                #Company_Profile.objects.create(c_name = request.POST.get('c_name'))

                #email for welcome
                subject = "Sahil Rajput, Engineering Tools"
                message = "Hello, " + data.c_name + ". Welcome To Engineering Tools :) :)"
                email_from = settings.EMAIL_HOST_USER
                email_to = [data.c_email,]
                send_mail(subject,message,email_from,email_to)
                #email logic complate

                return redirect('Company:Home')
    else:
        messages.error(request, 'Please Correct the error below.')
        r_form = register_form()

    return render(request, temp, {'register_form':r_form})



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
                    request.session["company_details"] = data.c_email
                    request.session["company_name"] = data.c_name
                    return redirect('Company:Home')
    else:
        l_form = login_form()

    return render(request, temp, {'login_form':l_form})



def Logout_view(request):
    temp = "Company/logout.html"
    if(request.session.get("company_details") != None):
        request.session.delete()
    else:
        return redirect('Company:Login')

    return render(request,temp,{})



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



def Edit_profile_view(request):
    temp = "Company/edit_profile.html"
    if request.method == 'POST':
        p_form = edit_profile_form(request.POST or None, request.FILES or None)
        if p_form.is_valid():
            profile_form = p_form.save(commit = False)
            profile_form.c_name = request.session.get('company_name')
            profile_form.save()
            return redirect('Company:Home')
    else:
        p_form = edit_profile_form()

    return render(request, temp, {'p_form':p_form})