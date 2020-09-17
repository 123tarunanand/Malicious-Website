from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('secure/', views.secure_view, name='secure_view')
]
