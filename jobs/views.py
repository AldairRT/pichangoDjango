from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from datetime import date, datetime, timedelta
from django.db.models import Q

from django.contrib import messages


from django.contrib.auth import authenticate, login, logout 

from django.contrib.auth.decorators import login_required

# Create your views here.

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        form = CreateUserForm
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, user + ' Tu cuenta ha sido creada')

                return redirect('login')

    context = {'form': form}
    return render(request,'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                messages.info(request, 'Tu nombre o clave es incorrecto')
    
    context= {}
    return render(request,'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')


def buscajuegos(request):
   q = request.GET.get('q', '')
   querys = (Q(cancha__nombre__icontains=q) | Q(cancha__distrito__icontains=q))
   buscajuegos = Juego.objects.filter(querys)
   context = {'data':buscajuegos}
   return render(request, 'buscajuegos.html', context)

def buscacanchas(request):
   q = request.GET.get('q', '')
   querys = (Q(nombre__icontains=q) | Q(distrito__icontains=q))
   buscacanchas = Cancha.objects.filter(querys)
   context = {'data':buscacanchas}
   return render(request, 'buscacanchas.html', context)


def home(request):
    startdate = datetime.today()
    enddate = startdate + timedelta(days=5)
    juegos = Juego.objects.filter(fecha__range=[startdate, enddate])
    context = {'data':juegos}
    return render(request, 'home.html', context)

def listajuegos(request):
    listajuegos = Juego.objects
    context = {'data':listajuegos}
    return render(request, 'listajuegos.html',context)

def detail(request,juego_id):
    juego_detail = get_object_or_404(Juego,pk=juego_id)
    context = {'data':juego_detail}
    return render(request,'juego.html', context)

def listacanchas(request):
    listacanchas = Cancha.objects
    context = {'data':listacanchas}
    return render(request, 'canchas.html',context)

def cancha_detail(request,cancha_id):
    cancha_detail = get_object_or_404(Cancha,pk=cancha_id)
    juegos_cancha = Juego.objects.filter(cancha=cancha_id)
    context = {'data':cancha_detail,'juegos':juegos_cancha}
    return render(request,'canchadetalle.html', context)


@login_required(login_url='login')
def profile(request):
    
    context = {}
    return render(request, 'profile.html', context)





