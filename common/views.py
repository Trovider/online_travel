from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from online_travel.models import Spot


def signup(request):
    """
    계정생성
    """
    spot = Spot.objects.all().values('country_name').distinct()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('common:login')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form, 'spot':spot})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('common:login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'common/change_password.html', {
        'form': form
    })


def change_interest(request):
    spot = Spot.objects.all().values('country_name').distinct()
    return render(request, 'common/change_interest.html', {'spot':spot})
