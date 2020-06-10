from django.shortcuts import render, redirect
from .models import Profile
# Create your views here.

def Home_View_User(request):
    temp = "User/index.html"
    return render(request, temp)

def My_Account_View(request):
    temp = "User/my_account.html"
    ID = request.user.id
    data = Profile.objects.get(user_id = ID)
    return render(request, temp, {'data':data})


def Update_Account_Info_View(request):
    if request.method == 'POST':
        number = request.POST.get("PhoneNumber")
        ID = request.user.id
        Profile.objects.filter(user_id=ID).update(phone=number)
        return redirect('User:Home')
    else:
        return redirect('User:My_Account')