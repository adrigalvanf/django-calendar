from django.urls import path
from . import views
app_name = 'usuario'

urlpatterns = [
    path('crear', views.crearusuario, name='crear'),
    path('iniciar',views.iniciar, name='iniciar'),
    path('salir',views.salir, name='salir'),
    path('logout', views.logt, name='logout')

    
]