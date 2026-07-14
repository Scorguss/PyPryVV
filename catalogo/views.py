from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import EBook

def lista_ebooks(request):
    """Muestra el catálogo de recursos publicados y permite buscar o filtrar."""
    # REGLA GHERKIN: Solo mostrar los en estado 'Publicado'
    ebooks = EBook.objects.filter(estado='Publicado')

    # Búsqueda por palabra clave o autor
    query = request.GET.get('q')
    categoria = request.GET.get('categoria')

    if query:
        ebooks = ebooks.filter(
            Q(titulo__icontains=query) |
            Q(autor_nombre__icontains=query)
        )

    if categoria:
        ebooks = ebooks.filter(categoria__iexact=categoria)

    return render(request, 'catalogo/lista_ebooks.html', {
        'ebooks': ebooks,
        'query': query,
        'categoria': categoria
    })

def detalle_ebook(request, pk):
    """Muestra la información completa de un eBook seleccionado."""
    ebook = get_object_or_404(EBook, pk=pk, estado='Publicado')
    return render(request, 'catalogo/detalle_ebook.html', {'ebook': ebook})