from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.SecureHomeView.as_view(), name='secure_home_view'),
    path('profile/<int:pk>/', views.SecureProfileView.as_view(), name='secure_profile_view'),
    path('search/', views.secure_search_view, name='secure_search_view'),
    path('login/', views.secure_login_view, name='secure_login_view'),
    path('logout/', views.secure_logout_view,name='secure_logout_view'),
    path('profileinfo/', views.SecureProfileInfoView.as_view(), name='secure_profileinfo_view')
]
