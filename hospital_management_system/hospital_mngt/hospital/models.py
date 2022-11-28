from django.db import models

# Create your models here.
class Doctore(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Contacto = models.CharField(max_length=12)
    Especialidad = models.CharField(max_length=50)
    
    def __str__(self):
        """String que representa al objeto Doctore"""
        return f'{self.Nombre} {self.Apellido}'
        
class Especialidade(models.Model):
    doctor = models.ForeignKey(Doctore, on_delete=models.CASCADE)
    TipoEspecialidad = models.CharField(max_length=50)
    
    def __str__(self):
        """String que representa al objeto Especialidad"""
        return f'{self.TipoEspecialidad}'
           