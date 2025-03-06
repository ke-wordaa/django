from django.urls import path
from . import views

urlpatterns = [
    path('show_all/', views.all_users_view, name='show_all'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.home, name='home'), # 範例首頁
]