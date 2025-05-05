from django.shortcuts import render, redirect 
from .forms.signup_form import SignupForm
from .forms.login_form import LoginForm
from django.contrib.auth import login,logout
from rest_framework.authtoken.models import Token


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')  # Redirect to login page after successful signup
    else:
        form = SignupForm()
    return render(request, 'account/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('account:profile')  # Redirect to a home page after successful login
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

def success_view(request):
    return render(request, 'account/success.html')

def logout_view(request):
    logout(request)
    return redirect('account:login')  # Redirect to login page after successful logout

def profile_view(request):
    if request.user.is_authenticated:
        try:
            token = Token.objects.get(user=request.user).key
        except Token.DoesNotExist:
            token = None
        return render(request, 'account/profile.html', {'user': request.user, 'token': token})
    else:
        return redirect('account:login')  # Redirect to login page if user is not authenticated
    
    
def generate_token_view(request):
    if request.user.is_authenticated:
        token, created = Token.objects.get_or_create(user=request.user)
        if created:
            token.save()  # Save the token if it was created
        return redirect('account:profile')  # Redirect to profile page after generating token
    else:
        return redirect('account:login')  # Redirect to login page if user is not authenticated
    