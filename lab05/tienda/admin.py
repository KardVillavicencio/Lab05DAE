from django.contrib import admin
from .models import Categoria, Producto, Cliente

admin.site.register(Categoria)
admin.site.register(Producto)

def marcar_como_verificado(modeladmin, request, queryset):
    queryset.update(verificado=True)

marcar_como_verificado.short_description = "Marcar como verificados"

# Definir la clase del administrador para el modelo Cliente
@admin.register(Cliente)
class ClienteAdminPersonalizado(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'dni', 'verificado')
    list_filter = ('verificado',)
    actions = [marcar_como_verificado]
    actions_on_bottom = True  # Muestra las acciones personalizadas en la parte inferior
