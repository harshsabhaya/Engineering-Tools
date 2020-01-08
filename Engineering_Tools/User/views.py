from django.shortcuts import render

# Create your views here.
def Home_View_User(request):
    temp = "User/index.html"
    return render(request, temp)