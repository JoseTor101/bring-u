from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .models import User  # Import your custom user model

def signup(request):
    data = {
        'form': SignUpForm()
    }
    if request.method == 'GET':
        return render(request, 'signup.html', data)
    else:
        if request.method == 'POST':
            user_creation_form = SignUpForm(request.POST)
            print(user_creation_form)
            
            if request.POST['password1'] == request.POST['password2']:
                print('YESSSSS')
                user_creation_form.save()

                #Logear al usuario inmediatamente después del registro
                user = authenticate(username = user_creation_form.cleaned_data['username'], password = user_creation_form.cleaned_data['password1'])
                login(request, user)
                return redirect('/')
            return render(request, 'signup.html', data)

"""def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'signupaccount.html', {'form': UserCreateForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    email=request.POST['email'],
                    password=request.POST['password1'],
                    name=request.POST['name'],
                    tel=request.POST['tel'],
                )
                user.save()
                login(request, user)
                return redirect('/')
            except IntegrityError:
                return render(request, 'signupaccount.html', {'form': UserCreateForm(), 'error': 'Username or email already taken. Choose a new one.'})
        else:
            return render(request, 'signupaccount.html', {'form': UserCreateForm(), 'error': 'Passwords do not match'})
"""

@login_required
def logoutaccount(request):
    logout(request)
    return redirect('/')


def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'loginaccount.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'loginaccount.html', {'form': AuthenticationForm(), 'error': 'Username and password do not match'})
        else:
            login(request, user)
            return redirect('/')
