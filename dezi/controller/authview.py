from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib import messages
from dezi.forms import CustomUserForm


def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Registered successfully! login to continue")
            return redirect('home')
    context = {'form': form}
    return render(request, 'dezi/auth/register.html', context)


def loginpage(request):
    # checks if user is already logged in
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in')
        return redirect('home')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            passwd = request.POST.get('password')

            user = authenticate(request, username=username, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'logged in successfully')
                return redirect('home')
            else:
                messages.error(request, "invalid username or password ")
                return redirect('loginpage')

        return render(request, 'dezi/auth/login.html')


def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'logged out successfully')
        return redirect('landingpage')
