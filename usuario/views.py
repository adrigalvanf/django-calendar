from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def crearusuario(request):
    if request.method == 'POST':
        usern=request.POST.get('username')
        mail=request.POST.get('email')
        paswrd=request.POST.get('password')
        user=User.objects.create_user(username=usern, email=mail, password=paswrd)
        user.save()
    return render(request, 'usuario/crear.html')

def iniciar(request):
    if request.method == 'POST':
        usern=request.POST.get('username')
        paswrd=request.POST.get('password')
        user = authenticate(request, username=usern, password=paswrd)
        login(request, user)
    return render(request,'usuario/iniciar.html')

def logt(request):
    return render(request, 'usuario/salir.html')

def salir(request):
    logout(request)
    return render(request,'inicio/inicio.html')
       


    

