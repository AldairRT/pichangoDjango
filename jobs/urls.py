from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name ="register"),
    path('login/', views.loginPage, name ="login"),
    path('logout/', views.logoutUser, name ="logout"),

    path('', views.home, name ="home"),
    path('listajuegos/', views.listajuegos, name ="listajuegos"),
    path('listajuegos/<int:juego_id>', views.detail,name='detail'),
    path('profile/', views.profile,name='profile')
]

