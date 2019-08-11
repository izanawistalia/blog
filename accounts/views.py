from django.shortcuts import render, redirect
from django.contrib.auth.models import User#importing necessary packages to create user account
from django.contrib import auth #importing auth package to help in authentication of user account

#method for signning up
def signup(request):
    if request.method == 'POST':
        #creating account
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'username already exists!!!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                auth.login(request, user)
                return redirect('home')

        else:
            return render(request, 'accounts/signup.html', {'error':'password does not match!!!'})

    else:
       return render(request, 'accounts/signup.html')


# method for logging up
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error':'username or password is incorrect!!!'})


    else:    
        return render(request, 'accounts/login.html')


# method for logging out
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

