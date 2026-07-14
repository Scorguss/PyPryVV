from behave import given, when, then
from behave.api.pending_step import StepNotImplementedError


# ==========================
# GIVEN
# ==========================

@given('que existen recursos académicos publicados')
def step_recursos_publicados(context):
    raise StepNotImplementedError()


@given('que existe un eBook publicado llamado "{titulo}"')
def step_ebook_publicado(context, titulo):
    raise StepNotImplementedError()


@given('que existe un eBook en estado "{estado}"')
def step_ebook_estado(context, estado):
    raise StepNotImplementedError()


# ==========================
# WHEN
# ==========================

@when('busco "{termino}"')
def step_busqueda(context, termino):
    raise StepNotImplementedError()


@when('busco recursos del autor "{autor}"')
def step_busqueda_autor(context, autor):
    raise StepNotImplementedError()


@when('filtro los recursos por la categoría "{categoria}"')
def step_filtrar_categoria(context, categoria):
    raise StepNotImplementedError()


@when('selecciono dicho eBook')
def step_seleccionar(context):
    raise StepNotImplementedError()


@when('exploro el catálogo')
def step_explorar(context):
    raise StepNotImplementedError()


# ==========================
# THEN
# ==========================

@then('deberían mostrarse los eBooks relacionados con "{termino}"')
def step_resultados(context, termino):
    raise StepNotImplementedError()


@then('solo deberían mostrarse recursos de esa categoría')
def step_categoria(context):
    raise StepNotImplementedError()


@then('deberían mostrarse únicamente sus publicaciones')
def step_publicaciones(context):
    raise StepNotImplementedError()


@then('el sistema debería indicar que no existen resultados')
def step_sin_resultados(context):
    raise StepNotImplementedError()


@then('debería visualizar su información completa')
def step_detalle(context):
    raise StepNotImplementedError()


@then('el eBook en estado "{estado}" no debería mostrarse')
def step_no_visible(context, estado):
    raise StepNotImplementedError()