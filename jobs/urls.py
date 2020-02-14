from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name ="register"),
    path('login/', views.loginPage, name ="login"),
    path('logout/', views.logoutUser, name ="logout"),

    path('', views.home, name ="home"),
    path('listajuegos/', views.listajuegos, name ="listajuegos"),
    path('buscajuegos/', views.buscajuegos, name ="buscajuegos"),
    path('buscacanchas/', views.buscacanchas, name ="buscacanchas"),
    path('listajuegos/<int:juego_id>', views.detail,name='detail'),
    path('listacanchas/', views.listacanchas, name ="listacanchas"),
    path('listacanchas/<int:cancha_id>', views.cancha_detail,name='cancha_detail'),
    path('profile/', views.profile,name='profile')
]

