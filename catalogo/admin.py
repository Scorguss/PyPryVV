from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import EBook, Capitulo

admin.site.register(EBook)
admin.site.register(Capitulo)