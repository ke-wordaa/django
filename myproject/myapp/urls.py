from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns =[
    path('', views.home_view, name='home'),  # 主页路由
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('update/', views.update_view, name='update'),  # 修正更新視圖的路由
    path('create/', views.create_view, name='create'),  # 新增資料的路由
    path('delete/', views.delete_view, name='delete'),  # 修正刪除視圖的路由
]
