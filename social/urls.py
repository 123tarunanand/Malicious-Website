from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home_view'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile_view'),
    path('search/', views.search_view, name='search_view'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view,name='logout_view')
]
