README DEL PROYECTO (TXT)
=====================================
Plataforma de Gestión de Productos — Django
Versión: 1.0
Desarrollado por: Marcelo Navarrete
Repositorio proyecto disponible en https://github.com/marchnav/M6_AE6_gestion_productos

DESCRIPCIÓN
-----------
Aplicación Django para gestionar productos con control de acceso por roles y permisos.
Incluye panel administrativo, modelo de productos, usuarios/grupos preconfigurados
y un Home público responsive hecho con TailwindCDN.

CARACTERÍSTICAS CLAVE
---------------------
- Autenticación y autorización con Django Admin.
- Roles por grupos: "Administradores", "Gestores de Productos", "Usuarios".
- Permisos granulares sobre Producto (view/add/change/delete).
- Modelo Producto con: nombre, descripción, precio, stock, fecha_creación.
- Semilla (seed) para crear usuarios de prueba y productos demo.
- Home público "/" con catálogo de productos recientes.
- Branding del Django Admin y menú de acceso rápido.

TECNOLOGÍAS
-----------
- Python 3.13 (compatible 3.12+)
- Django 5.2.x
- SQLite (por defecto; fácilmente portable a PostgreSQL/MySQL)
- TailwindCSS vía CDN en templates públicos

ESTRUCTURA (RESUMEN)
--------------------
config/                 # Proyecto Django
  settings.py
  urls.py               # Incluye productos.urls (home)
productos/              # App de negocio
  admin.py              # Registro y personalización del admin
  models.py             # Modelo Producto
  views.py              # Vista home
  urls.py               # Rutas de la app
  templates/productos/home.html
  management/commands/seed_demo.py  # Carga inicial de grupos/usuarios/productos
requirements.txt (opcional)
README_RUBRICA.txt      # Evidencia de rúbrica (este repo)

INSTALACIÓN Y EJECUCIÓN (WINDOWS POWERSHELL)
--------------------------------------------
1) Crear y activar entorno virtual
   python -m venv .venv
   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
   .\.venv\Scripts\Activate.ps1

2) Instalar dependencias (si existe requirements.txt)
   pip install -r requirements.txt

3) Migraciones
   python manage.py makemigrations
   python manage.py migrate

4) Semilla de datos (grupos/usuarios/productos)
   python manage.py seed_demo

5) Crear superusuario
   python manage.py createsuperuser

6) Ejecutar servidor
   python manage.py runserver
   Abrir: http://127.0.0.1:8000/  (Home)
          http://127.0.0.1:8000/admin/  (Panel)

USUARIOS/ROLES POR DEFECTO (SEED)
---------------------------------
- Grupo "Administradores": CRUD completo de Producto.
- Grupo "Gestores de Productos": view, add, change (SIN delete).
- Grupo "Usuarios": solo view.

Cuentas de prueba creadas por seed_demo:
- gestor1 / demo12345  → is_staff=True, accede al admin, agrega/modifica, NO borra.
- usuario1 / demo12345 → is_staff=False, NO accede al admin, rol de lectura (fuera del admin).
(Adicional) Durante pruebas se creó "viewer1" como staff con grupo "Usuarios" → solo lectura en admin.

MODELO PRODUCTO
---------------
- nombre: CharField
- descripcion: TextField/CharField largo
- precio: DecimalField
- stock: IntegerField
- fecha_creacion: DateTimeField(auto_now_add=True)

ADMINISTRACIÓN
--------------
- /admin/ → requiere is_staff=True para acceder.
- Permisos de objeto por grupo determinan qué acciones aparecen (Add, Save, Delete).
- Branding visible en cabecera del admin.

FRONTEND
--------
- Ruta raíz "/": listado de hasta 8 productos recientes en cards.
- Tailwind vía CDN; diseño responsive y ligero.
- Enlace directo al admin en la navbar.

TAREAS COMUNES
--------------
- Ejecutar tests (si aplica): python manage.py test
- Crear app nueva: python manage.py startapp <nombre>
- Crear migración manual: python manage.py makemigrations
- Aplicar migraciones: python manage.py migrate
- Crear superusuario: python manage.py createsuperuser

SOLUCIÓN DE PROBLEMAS
---------------------
- Política de ejecución en PowerShell bloquea activar venv:
  Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

- “No module named django”:
  Activar venv y ejecutar: pip install -r requirements.txt  (o pip install django)

- Migraciones/DB inconsistentes en desarrollo:
  Cerrar servidor, borrar db.sqlite3 (solo local) y migraciones de app, luego:
  python manage.py makemigrations && python manage.py migrate && python manage.py seed_demo

- Tailwind CDN no carga en redes restringidas:
  Verificar acceso a cdn.tailwindcss.com o instalar Tailwind localmente.

SEGURIDAD (NOTAS)
-----------------
- Nunca subir `.env` ni claves a repositorios públicos.
- En producción usar HTTPS, cabeceras de seguridad (CSP, HSTS), y DB gestionada.
- Crear usuarios con contraseñas robustas y deshabilitar cuentas de demo.

ROADMAP (IDEAS FUTURAS)
-----------------------
- Paginación y filtros en Home.
- Vista pública de detalle de producto (read-only).
- Auditoría de cambios (django-simple-history).
- API REST con Django REST Framework para integraciones.

LICENCIA
--------
Todos los derechos reservados. Uso exclusivo para evaluación académica del bootcamp Skillnest,
salvo autorización escrita del autor.

CONTACTO
--------
marcelo.navarrete (marcelonavarretey@gmail.com)


