from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_ebooks, name='lista_ebooks'),
    path('ebook/<int:pk>/', views.detalle_ebook, name='detalle_ebook'),
]