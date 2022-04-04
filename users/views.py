from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm
from django.utils.translation import gettext_lazy as _

# Create your views here.


@login_required(login_url='login')
def welcome(requrest):
    
    return render(requrest, './users/welcome.html')

@login_required(login_url='login')
def user_update(request,id):
    # respondents=Respondent.objects.all()
    user=Profile.objects.get(id=id)
    # citys=City.objects.all()
    message=None
    _params = {
        "title": _('資訊修改'),
        "message":message, 
    }

    if request.method=='POST':
        new_email=request.POST.get('new-email')
        # respondent_id=request.POST.get('respondent-id')
        # city_id=request.POST.get('city-id')

        # print(new_email,respondent_id)

        if not new_email:
            message='請輸入Email'
        # Email不能重複(除非是本身的email)
        elif not Profile.objects.filter(email=new_email) or user.email==new_email:
            user.email=new_email
            # user.respondent=Respondent.objects.get(id=respondent_id)
            # user.city=City.objects.get(id=city_id)
            user.save()
            message='資料更新成功!'

            return redirect('profile', id=user.id)

        else:
            message='Email已經註冊'

    return render(request,'./users/update.html', _params)


def user_login(request):
    username, password, message = '', '', ''
    _params={
        'title': "HIKARINOHOUSE",
        'id': _("帳號"),
        'pw': _("密碼"),
        'username': username, 
        'password': password,
        'message': message,
    }

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

    return render(request, './users/login.html', _params)



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
    _params = {
        "title": _('使用者資訊'),
        "user": user,
    }
    # print(user)
    return render(request, './users/profile.html', _params)
