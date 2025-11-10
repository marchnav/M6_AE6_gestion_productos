from django.shortcuts import render
from .models import Producto

def home(request):
    productos = Producto.objects.order_by('-fecha_creacion')[:8]
    return render(request, 'productos/home.html', {'productos': productos})
