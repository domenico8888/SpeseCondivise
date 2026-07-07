from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('users/', views.users, name='users'),
    path('users/add/', views.add_user, name='add_user'),
path("expenses/", views.expenses, name="expenses"),
]