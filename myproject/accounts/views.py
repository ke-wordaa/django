from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm  # 使用內建的登入表單
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegistrationForm  # 導入 RegistrationForm

 # 註冊視圖
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

 # 登入視圖
def user_login(request):
     if request.method == 'POST':
         form = AuthenticationForm(request, data=request.POST)  # 使用 AuthenticationForm
         if form.is_valid():
             user = form.get_user()
             login(request, user)
             return redirect('home')
     else:
         form = AuthenticationForm(request)  # 傳遞 request
     return render(request, 'accounts/login.html', {'form': form})

 # 登出視圖
def user_logout(request):
     logout(request)
     return redirect('home')

 # 首頁視圖 (範例)

def home(request):
    return render(request, 'accounts/home.html')
@login_required
def all_users_view(request):
    users = User.objects.all()
    return render(request, 'accounts/show.html', {'users': users})
 