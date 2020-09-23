from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from student.models import first_year, second_year, third_year

# Create your views here.

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return render(request, 'login.html')

def handellogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']

        user = authenticate(username=username, password = password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('dashboard')

    return render(request, 'login.html')

def handellogout(request):
    logout(request)
    return redirect('dashboard')

def resultupload(request):
    pass
