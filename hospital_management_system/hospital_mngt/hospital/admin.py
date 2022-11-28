from django.contrib import admin
from.models import Doctore, Paciente, Cita

# Define la clase admin para Doctore
class DoctoreAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Apellido')
    list_filter = ('Apellido')
    fieldsets = (
        ('Información Personal',{
            'fields':('Nombre', 'Apellido')
        }),
        ('Información Adicional',{
            'fields':('Contacto', 'Especialidad')
        }),
    )
    
# Define la clase admin para Paciente
class DoctoreAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Apellido')
    list_filter = ('Apellido')
    fieldsets = (
        ('Información Personal',{
            'fields':('Nombre', 'Apellido', 'Genero')
        }),
        ('Información Adicional',{
            'fields':('Contacto', 'Email', 'Direccion')
        }),
    )
    

    
# Define la clase admin para Cita
class DoctoreAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Apellido')
    list_filter = ('Apellido')
    fieldsets = (
        ('Información Personal',{
            'fields':('doctor', 'paciente')
        }),
        ('Información Adicional',{
            'fields':('datos', 'tiempo')
        }),
    )


# Register your models here.
admin.site.register(Doctore)
admin.site.register(Paciente)
admin.site.register(Cita)


    
