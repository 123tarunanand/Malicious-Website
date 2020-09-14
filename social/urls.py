from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('profile/', views.ProfileView.as_view(), name='profile_view'),
    path('search/', views.search_view, name='search_view'),
    path('login/', views.login_view, name='login_view')
]
