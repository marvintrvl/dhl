from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('orders/', views.order_list, name='order_list'),
    path('order/<str:order_id>/', views.order_detail, name='order_detail'),
    path('balance/', views.user_balance, name='user_balance'),
    path('order/<str:order_id>/', views.order_detail, name='order_detail'),
    path('details/', views.details, name='details'),
    path('scan/<str:package_id>/', views.scan_qr_code, name='scan_qr_code'),
    path('scan-success/', views.scan_success, name='scan_success'),
]
