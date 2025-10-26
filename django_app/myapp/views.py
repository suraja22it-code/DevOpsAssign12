from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

def index(request):
    """Redirect to login page"""
    return redirect('login')

def login_view(request):
    """Handle login page and authentication"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    
    return render(request, 'login.html')

def register_view(request):
    """Handle user registration"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        from django.contrib.auth.models import User
        
        try:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            else:
                user = User.objects.create_user(username=username, password=password)
                messages.success(request, 'Registration successful! Please login.')
                return redirect('login')
        except Exception as e:
            messages.error(request, f'Registration error: {str(e)}')
    
    return render(request, 'register.html')

@login_required
def home_view(request):
    """Home page - requires login"""
    username = request.user.username
    return render(request, 'home.html', {'username': username})

def logout_view(request):
    """Handle logout"""
    logout(request)
    return redirect('login')