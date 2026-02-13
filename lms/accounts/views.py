from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        role = request.POST.get('role', 'student')
        
        # Validation
        if not username or not password:
            messages.error(request, 'Username and password are required.')
            return render(request, 'accounts/register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different one.')
            return render(request, 'accounts/register.html')
        
        try:
            user = User.objects.create_user(username=username, password=password)
            profile = Profile.objects.create(user=user, role=role)
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('accounts:login')
        except Exception as e:
            messages.error(request, f'An error occurred during registration: {str(e)}')
            return render(request, 'accounts/register.html')
    
    return render(request, 'accounts/register.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('core:dashboard')
    return render(request, 'accounts/login.html')
def logout_view(request):
    logout(request)
    return redirect('accounts:login')
