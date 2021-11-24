from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from accounts.forms import CreateUserForm


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account was created for' + form.cleaned_data.get('username'))
                return redirect('login')
            context = {'form': form}
            return render(request, "accounts/register.html", context)
        else:
            form = CreateUserForm()
            context = {'form': form}
            return render(request, "accounts/register.html", context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username or password is incorrect')
        context = {}
        return render(request, "accounts/login.html", context)


def logoutPage(request):
    logout(request)
    return redirect('login')
