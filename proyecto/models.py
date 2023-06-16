from django.db import models
from django.contrib.auth.models import User
from schedule.models import Calendar

# Create your models here.
class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    inicio = models.DateField()
    final = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='proyectos_creados')
    descripcion = models.TextField()

def __iter__(self):
        proyectos_usuario = Proyecto.objects.filter(user=self.user)
        return iter(proyectos_usuario)

class Tarea(models.Model):
      proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
      tarea = models.CharField(max_length=200)
      dia=models.DateField()
      user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='tareas')





