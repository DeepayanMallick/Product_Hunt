from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from . forms import SignUpForm, EditProfileForm


def profile(request):
    return render(request, 'accounts/profile.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'You Have Been Logged in!')
            return redirect('home')
        else:
            messages.warning(request, f'Error Logging In - Please Try Again...')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html', {})

def logout_user(request):
    logout(request)
    messages.warning(request, f'You Have Been Logged Out! Please Login To stay connected...')
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'You Have Been Registered Successfully!')
            return redirect('home')
    else:
        form = SignUpForm()
        
    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'You Have Been Edited Your Profile Successfully!')
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
        
    context = {'form': form}
    return render(request, 'accounts/edit_profile.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, f'You Have Been Edited Your Password Successfully!')
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
        
    context = {'form': form}
    return render(request, 'accounts/change_password.html', context)

