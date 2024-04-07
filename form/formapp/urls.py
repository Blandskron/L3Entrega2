from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulario, name='formulario'),
    path('formulario-exitoso/', views.formulario_exitoso, name='formulario_exitoso'),
]
