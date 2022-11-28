from django.contrib import admin
from.models import Doctore, Especialidade

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
    
# Define la clase admin para Especialidad
class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('Especialidad')
    list_filter = ('doctor')
    fieldsets = (
        ('Información Personal',{
            'fields':('doctor')
        })
    )
    

# Register your models here.
admin.site.register(Doctore)
admin.site.register(Especialidade)


    
