from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Register, Company_Profile
from .forms import register_form, login_form, profile_form

# Create your views here.
def Home_View_Company(request):
    temp = "Company/index.html"
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
                Company_Profile.objects.create(c_name = request.POST.get('c_name'))
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


def Profile_view(request):
    temp = "Company/profile.html"
    p_form = profile_form()
    return render(request, temp, {'p_form':p_form})