from django.urls import path
from . import views
app_name = 'proyecto'

urlpatterns = [
    path('', views.nuevo, name=''),
    path('nuevo', views.projectnew, name='nuevo'),
    path('calendario/', views.calendar_variable, name='calendario'),
    path('evento', views.crear_evento, name='evento'),
    
    
]