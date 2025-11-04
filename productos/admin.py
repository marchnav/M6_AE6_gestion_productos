from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "precio", "stock", "fecha_creacion")
    list_display_links = ("id", "nombre")
    search_fields = ("nombre", "descripcion")
    list_filter = ("fecha_creacion",)
    ordering = ("-fecha_creacion",)
    readonly_fields = ("fecha_creacion",)
    list_per_page = 25
    date_hierarchy = "fecha_creacion"

    def has_delete_permission(self, request, obj=None):
        # Solo permite borrar a quien tenga el permiso explícito
        return request.user.has_perm('productos.delete_producto')

    def get_actions(self, request):
        # Oculta la acción masiva "Eliminar seleccionados" si no tiene permiso de borrado
        actions = super().get_actions(request)
        if not request.user.has_perm('productos.delete_producto'):
            actions.pop('delete_selected', None)
        return actions
