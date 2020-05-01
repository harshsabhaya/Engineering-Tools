from django.shortcuts import render

# Create your views here.
def ET_login(request):
    temp = "ET_Admin/login.html"
    return render(request,temp)