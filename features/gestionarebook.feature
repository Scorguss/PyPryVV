# language: es

Característica: Crear y publicar eBooks
  Como autor académico
  Quiero crear y publicar eBooks
  Para compartir recursos educativos con la comunidad académica.

  Antecedentes:
    Dado que soy un usuario autenticado con rol "Autor"

  Escenario: Crear un eBook con información válida
    Cuando registro un eBook con título "Introducción a Django"
    Y ingreso una descripción válida
    Y agrego al menos un capítulo
    Entonces el eBook debería guardarse en estado "Borrador"

  Escenario: Publicar un eBook correctamente
    Dado que existe un eBook en estado "Borrador"
    Cuando selecciono la opción "Publicar"
    Entonces el eBook debería cambiar al estado "Publicado"
    Y debería estar disponible en el catálogo académico

  Escenario: Intentar publicar un eBook sin capítulos
    Dado que existe un eBook en estado "Borrador"
    Y el eBook no tiene capítulos
    Cuando intento publicarlo
    Entonces el sistema debería impedir la publicación
    Y debería mostrar el mensaje "El eBook debe contener al menos un capítulo."

  Escenario: Intentar crear un eBook sin título
    Cuando registro un eBook sin título
    Entonces el sistema debería mostrar el mensaje "El título es obligatorio."

  Escenario: Intentar crear un eBook con un título duplicado
    Dado que ya existe un eBook llamado "Introducción a Django"
    Cuando registro un nuevo eBook con el mismo título
    Entonces el sistema debería impedir el registro
    Y debería mostrar el mensaje "Ya existe un eBook con ese título."

  Escenario: Usuario sin permisos intenta publicar un eBook
    Dado que soy un usuario autenticado con rol "Estudiante"
    Y existe un eBook en estado "Borrador"
    Cuando intento publicarlo
    Entonces el sistema debería denegar la acción
    Y debería mostrar el mensaje "No tiene permisos para publicar este eBook."