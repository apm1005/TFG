from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterFrom


def register(request):
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! Log in!')
            return redirect('login')
    else:
        form = UserRegisterFrom()
    return render(request, 'users/register.html', {'form': form})
