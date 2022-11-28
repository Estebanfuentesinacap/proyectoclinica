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
    
class Paciente(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Genero = models.CharField(max_length=10)
    Contacto = models.IntegerField(null=True)
    Email = models.EmailField()
    Direccion = models.CharField(max_length=50)
    
    def __str__(self):
        """String que representa al objeto Paciente"""
        return f'{self.Nombre} {self.Apellido}'
    
class Cita(models.Model):
    doctor = models.ForeignKey(Doctore, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    datos = models.TextField()
    tiempo = models.TimeField()