from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('booking/', views.booking, name='booking'),
    path('login/', views.signin, name='login'),
    path('celebrities/', views.celebrities, name='celebrities'),
    path('payment/<int:amount>', views.payment, name='payment'),


    path('dashboard/', views.dashboard, name="dashboard"),
    path('clients/', views.client, name="clients"),
    path('bookings/', views.admin_booking, name="bookings"),
    path('password-change/', views.password_change, name="password_change"),
    path('discounts/', views.discount, name="discounts"),
    path('discount-form/', views.discount_form, name="discount_form"),
]