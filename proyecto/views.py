from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Proyecto, Tarea
from schedule.models import  Calendar, Event
from django.utils.dateparse import parse_datetime
from django.contrib.auth.models import User
import calendar

# Create your views here.
@login_required(login_url='usuario:iniciar')
def nuevo(request):
    project=Proyecto.objects.filter(user=request.user)
    proyectos= project.order_by('inicio')
    return render(request, 'proyecto/nuevo.html',{'proyectos':proyectos})

@login_required(login_url='usuario:iniciar')
def projectnew(request):
    if request.method == 'POST':
        titulo=request.POST.get('titulo')
        inicio=request.POST.get('inicio')
        final=request.POST.get('final')
        descripcin = request.POST.get('descripcion')
        
        proyecto = Proyecto(titulo=titulo, inicio=inicio, final=final, user=request.user, descripcion= descripcin)
        proyecto.save()
        project=Proyecto.objects.filter(user=request.user)
        proyectos= project.order_by('inicio')
    return render(request, 'proyecto/nuevo.html',{'proyectos':proyectos})

@login_required(login_url='usuario:iniciar')
def crear_evento(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        start_date = request.POST.get('start_date')
        start_time = request.POST.get('start_time')
        end_date = request.POST.get('end_date')
        end_time = request.POST.get('end_time')
        

        # Convierte la fecha y hora en un objeto de fecha y tiempo
        start = parse_datetime(f'{start_date}T{start_time}')
        end = parse_datetime(f'{end_date}T{end_time}')
        
        # Crea un nuevo evento y guárdalo en la base de datos
        evento = Event(title=title, start=start, end=end, calendar_id='1', creator=request.user, color_event='011')
        evento.save()

    return render(request, 'proyecto/nuevo.html')

@login_required(login_url='usuario:iniciar')
def calendar_variable(request):
    if request.method == 'GET':
        year = int(request.GET.get('year', 2023))  # Obtener el valor del año de la solicitud GET
        month = int(request.GET.get('month', 6))  # Obtener el valor del mes de la solicitud GET
    else:
        year = 2023  # Valor predeterminado en caso de que no se proporcione el año
        month = 6  # Valor predeterminado en caso de que no se proporcione el mes
    cal=calendar.Calendar(firstweekday=0)
    vista_calendario = cal.monthdatescalendar(year, month)
    proyectos=Proyecto.objects.filter(user=request.user)

    # Imprimir la vista de calendario

    context = {
        'calendario': vista_calendario,
        'proyectos': proyectos
    }
     
    return render(request, 'proyecto/calendario.html', context)

@login_required(login_url='usuario:iniciar')   
def project_view(request):
    proyectos=Proyecto.objects.filter(user=request.user)
    return render(request, 'proyecto/nuevo.html', {'proyectos':proyectos} )


    
