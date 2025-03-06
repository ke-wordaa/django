from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Myappdata
from django.http import JsonResponse

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # 登录成功后跳转到主页
    else:
        form = AuthenticationForm()

    return render(request, 'myapp/login.html', {'form': form})

# 登出视图
def logout_view(request):
    logout(request)
    return redirect('login')  # 登出后重定向到登录页面

@login_required
def home_view(request):
    list = Myappdata.objects.all().values()  # 取得所有的 data 資訊
    # mysql_loads = mysql_load.objects.filter(user=request.user)  # 取得當前用戶的 mysql_load 資訊
    return render(request, 'myapp/home.html', {'list':list})  # 傳遞 data_list 給模板

@login_required
def update_view(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        description = request.POST.get('description')
        
        try:
            data = Myappdata.objects.get(id=id)
            data.name = name
            data.description = description
            data.save()
            return JsonResponse({'status': 'success'})
        except Myappdata.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'data not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

@login_required
def create_view(request):
    if request.method == 'POST':
        id = request.POST.get('id')  # 新增指定 ID
        name = request.POST.get('name')
        description = request.POST.get('description')
        
        Myappdata.objects.create(id=id, name=name, description=description)  # 使用指定 ID
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

@login_required
def delete_view(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        
        try:
            data = Myappdata.objects.get(id=id)
            data.delete()
            return JsonResponse({'status': 'success'})
        except Myappdata.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'data not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

