from behave import given, when, then
from behave.api.pending_step import StepNotImplementedError


# ==========================
# GIVEN
# ==========================

@given('que soy un usuario autenticado con rol "{rol}"')
def step_usuario_autenticado(context, rol):
    raise StepNotImplementedError()


@given('que existe un eBook en estado "{estado}"')
def step_ebook_estado(context, estado):
    raise StepNotImplementedError()


@given('el eBook no tiene capítulos')
def step_sin_capitulos(context):
    raise StepNotImplementedError()


@given('que ya existe un eBook llamado "{titulo}"')
def step_ebook_existente(context, titulo):
    raise StepNotImplementedError()


# ==========================
# WHEN
# ==========================

@when('registro un eBook con título "{titulo}"')
def step_registrar_ebook(context, titulo):
    raise StepNotImplementedError()


@when('ingreso una descripción válida')
def step_descripcion(context):
    raise StepNotImplementedError()


@when('agrego al menos un capítulo')
def step_agregar_capitulo(context):
    raise StepNotImplementedError()


@when('registro un eBook sin título')
def step_sin_titulo(context):
    raise StepNotImplementedError()


@when('registro un nuevo eBook con el mismo título')
def step_titulo_duplicado(context):
    raise StepNotImplementedError()


@when('publico el eBook')
def step_publicar(context):
    raise StepNotImplementedError()


@when('intento publicarlo')
def step_intentar_publicar(context):
    raise StepNotImplementedError()


# ==========================
# THEN
# ==========================

@then('el eBook debería guardarse en estado "{estado}"')
def step_verificar_estado(context, estado):
    raise StepNotImplementedError()


@then('el eBook debería cambiar al estado "{estado}"')
def step_estado_publicado(context, estado):
    raise StepNotImplementedError()


@then('debería estar disponible en el catálogo académico')
def step_disponible_catalogo(context):
    raise StepNotImplementedError()


@then('el sistema debería impedir la publicación')
def step_publicacion_denegada(context):
    raise StepNotImplementedError()


@then('el sistema debería impedir el registro')
def step_registro_denegado(context):
    raise StepNotImplementedError()


@then('el sistema debería denegar la acción')
def step_denegar_accion(context):
    raise StepNotImplementedError()


@then('debería mostrar el mensaje "{mensaje}"')
def step_mensaje(context, mensaje):
    raise StepNotImplementedError()