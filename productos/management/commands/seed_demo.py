from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from productos.models import Producto
from django.db import transaction

class Command(BaseCommand):
    help = "Crea grupos, asigna permisos, usuarios de prueba y productos demo."

    @transaction.atomic
    def handle(self, *args, **options):
        # === Permisos del modelo Producto ===
        ct = ContentType.objects.get_for_model(Producto)
        perm_view   = Permission.objects.get(codename="view_producto", content_type=ct)
        perm_add    = Permission.objects.get(codename="add_producto", content_type=ct)
        perm_change = Permission.objects.get(codename="change_producto", content_type=ct)
        perm_delete = Permission.objects.get(codename="delete_producto", content_type=ct)

        # === Grupos ===
        admin_group, _ = Group.objects.get_or_create(name="Administradores")
        gestores_group, _ = Group.objects.get_or_create(name="Gestores de Productos")
        usuarios_group, _ = Group.objects.get_or_create(name="Usuarios")

        # Asignación de permisos por grupo
        # Administradores: view, add, change, delete
        admin_group.permissions.set([perm_view, perm_add, perm_change, perm_delete])

        # Gestores de Productos: view, add, change (SIN delete)
        gestores_group.permissions.set([perm_view, perm_add, perm_change])

        # Usuarios: solo view
        usuarios_group.permissions.set([perm_view])

        self.stdout.write(self.style.SUCCESS("Grupos y permisos configurados."))

        # === Usuarios de prueba ===
        # Nota: La rúbrica pide crear el superusuario con 'createsuperuser', lo dejaremos fuera del seed.
        # Creamos 2 usuarios de prueba: gestor1 y usuario1
        if not User.objects.filter(username="gestor1").exists():
            u = User.objects.create_user(username="gestor1", email="gestor1@example.com", password="demo12345")
            u.first_name = "Gestor"
            u.last_name = "Demo"
            u.is_staff = True  # para acceder al admin
            u.save()
            u.groups.add(gestores_group)

        if not User.objects.filter(username="usuario1").exists():
            u = User.objects.create_user(username="usuario1", email="usuario1@example.com", password="demo12345")
            u.first_name = "Usuario"
            u.last_name = "Demo"
            u.is_staff = False  # no puede entrar al admin
            u.save()
            u.groups.add(usuarios_group)

        self.stdout.write(self.style.SUCCESS("Usuarios de prueba creados/asignados a grupos."))

        # === Productos demo ===
        productos_demo = [
            {"nombre": "Teclado Mecánico", "descripcion": "Switches azules, retroiluminado.", "precio": "49990", "stock": 25},
            {"nombre": "Mouse Inalámbrico", "descripcion": "Sensor óptico de alta precisión.", "precio": "19990", "stock": 60},
            {"nombre": "Monitor 24''", "descripcion": "IPS 75Hz con filtro de luz azul.", "precio": "129990", "stock": 12},
            {"nombre": "Audífonos Over-Ear", "descripcion": "Cancelación de ruido pasiva.", "precio": "34990", "stock": 40},
            {"nombre": "Webcam FHD", "descripcion": "1080p con micrófono integrado.", "precio": "25990", "stock": 30},
        ]

        creados = 0
        for p in productos_demo:
            if not Producto.objects.filter(nombre=p["nombre"]).exists():
                Producto.objects.create(
                    nombre=p["nombre"],
                    descripcion=p["descripcion"],
                    precio=p["precio"],
                    stock=p["stock"]
                )
                creados += 1

        self.stdout.write(self.style.SUCCESS(f"Productos demo creados: {creados} (si ya existían, no se duplican)."))

        # === Resumen útil en consola ===
        self.stdout.write(self.style.SUCCESS("\n=== CREDENCIALES DE PRUEBA ==="))
        self.stdout.write("gestor1 / demo12345  -> Acceso admin, puede agregar y modificar, NO borrar.")
        self.stdout.write("usuario1 / demo12345 -> NO accede al admin (solo permisos de lectura por grupo).")
        self.stdout.write(self.style.SUCCESS("\nListo. Ahora crea el superusuario con 'python manage.py createsuperuser'."))

