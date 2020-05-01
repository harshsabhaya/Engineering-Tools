from django.shortcuts import render, redirect

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