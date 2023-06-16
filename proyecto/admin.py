from django.contrib import admin



# Register your models here.
from .models import Proyecto, Tarea

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'inicio', 'final', 'user', 'descripcion')
    list_filter = ('user', 'titulo')
    search_fields = ('titulo', 'user__username')

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('proyecto', 'tarea', 'dia', 'user')
    list_filter = ('proyecto', 'dia')
    search_fields = ('proyecto', 'user__username')



