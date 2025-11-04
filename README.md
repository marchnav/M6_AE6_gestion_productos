# Plataforma de Gestión de Productos (Django)

Panel administrativo para crear, editar, listar y (según permisos) eliminar productos, utilizando **Django 5.2.7** y el sistema nativo de **auth, groups y permissions**.

## Requisitos
- Python 3.11+ (recomendado)
- Pip actualizado

## Configuración rápida

# 1) Crear y activar entorno
py -m venv .venv
.\.venv\Scripts\Activate.ps1   # Windows PowerShell

# 2) Instalar dependencias
pip install django==5.2.7

# 3) Crear proyecto (si no existe) y app
django-admin startproject config .
python manage.py startapp productos

# 4) Migraciones
python manage.py makemigrations
python manage.py migrate

# 5) Superusuario
python manage.py createsuperuser

# 6) Ejecutar servidor
python manage.py runserver

## Modelo Producto
Campos básicos:

nombre (CharField)

descripcion (TextField)

precio (DecimalField)

stock (PositiveIntegerField)

fecha_creacion (DateTimeField, auto_now_auto_add=True)

Ordenado por -fecha_creacion. Registrado en el admin con búsqueda, filtros, paginación y jerarquía por fecha.

## Admin y permisos


# Grupos

Administradores: add/change/delete/view sobre productos | producto.

Gestores de Productos: add/change/view (sin delete).

Usuarios de ejemplo (sugeridos)

admin_local → is_staff ✅, grupo Administradores.

gestor1 → is_staff ✅, grupo Gestores de Productos.

viewer1 → is_staff ✅, permiso individual view en Producto.

# Reglas aplicadas en el admin

Solo puede borrar quien tenga el permiso productos.delete_producto.

Se oculta la acción masiva Eliminar seleccionados si el usuario no tiene permiso de borrado.

Página 403 personalizada cuando se intenta borrar sin permiso o acceder a vistas restringidas.

# Branding del admin:

site_header = "Plataforma de Gestión de Productos"

site_title = "Panel de Administración"

index_title = "Dashboard"

## Pruebas manuales de permisos

Crear producto con superusuario.

Ingresar como admin_local → debe poder borrar.

Ingresar como gestor1 → no debe ver opción de borrado; forzar /delete/ debe devolver 403.

Ingresar como viewer1 → solo lectura, sin botones de guardar.
