from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Juego, Cancha, Jugador
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from datetime import date, datetime, timedelta

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


def home(request):
    startdate = datetime.today()
    enddate = startdate + timedelta(days=1)
    juegos = Juego.objects.filter(fecha__range=[startdate, enddate])
    context = {'data':juegos}
    return render(request, 'home.html', context)

def listajuegos(request):
    listajuegos = Juego.objects

    context = {'data':listajuegos}
    return render(request, 'listajuegos.html',context)

def detail(request,juego_id):
    listacanchas= Cancha.objects
    juego_detail = get_object_or_404(Juego,pk=juego_id)

    context = {'data':juego_detail}
    return render(request,'juego.html', context)

@login_required(login_url='login')
def profile(request):
    
    context = {}
    return render(request, 'profile.html', context)





