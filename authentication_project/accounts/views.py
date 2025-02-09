from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm

# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('login')
    else:
        form = SignupForm()  

    return render(request, 'accounts/signup.html', {'form': form}) 


def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():  
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')

    return render(request, 'accounts/login.html', {'form': form})

@login_required
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html', {'user': request.user})

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
