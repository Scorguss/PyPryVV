# language: es

Característica: Explorar catálogo académico
  Como usuario
  Quiero buscar y explorar recursos académicos
  Para encontrar contenido relevante para mi aprendizaje.

  Antecedentes:
    Dado que existen recursos académicos publicados

  Escenario: Buscar un eBook por título
    Cuando busco "Django"
    Entonces deberían mostrarse los eBooks relacionados con "Django"

  Escenario: Buscar recursos por categoría
    Cuando filtro los recursos por la categoría "Ingeniería de Software"
    Entonces solo deberían mostrarse recursos de esa categoría

  Escenario: Buscar recursos por autor
    Cuando busco recursos del autor "Juan Pérez"
    Entonces deberían mostrarse únicamente sus publicaciones

  Escenario: Buscar un recurso inexistente
    Cuando busco "Computación Cuántica para Niños"
    Entonces el sistema debería indicar que no existen resultados

  Escenario: Visualizar el detalle de un recurso
    Dado que existe un eBook publicado llamado "Introducción a Django"
    Cuando selecciono dicho eBook
    Entonces debería visualizar su información completa

  Escenario: Explorar únicamente recursos publicados
    Dado que existe un eBook en estado "Borrador"
    Cuando exploro el catálogo
    Entonces el eBook en estado "Borrador" no debería mostrarse