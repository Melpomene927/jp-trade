from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

# Create your views here.


@login_required(login_url='login')
def welcome(requrest):
    
    return render(requrest, './users/welcome.html')


def user_login(request):
    username, password, message = '', '', ''

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username, password)
        user = authenticate(request, username=username, password=password)
        # print(user)
        if user:
            login(request, user)  # request.user
            return redirect('welcome')

        #帳號錯誤
        if Profile.objects.filter(username=username).exists():
            message = '密碼錯誤'
        else:
            message = '帳號錯誤'

    return render(request, './users/login.html', {'username': username, 'password': password,
                                                 'message': message})



@login_required(login_url='login')
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('login')


def user_register(request):
    if request.method == 'GET':
        form = ProfileForm()

    elif request.method == 'POST':
        print(request.POST)
        form = ProfileForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)  # request.user
            return redirect('welcome')

    return render(request, './users/register.html', {'form': form})


def profile(request,id):
    user = Profile.objects.get(id=id)
    # print(user)
    return render(request, './users/profile.html', {'user': user})
