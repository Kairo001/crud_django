"""Urls de la app de crud_empresa."""

# Django
from django.urls import path

# Vistas
from crud_empresa import views

urlpatterns = [
    path('', views.EmpresaCreateView.as_view(), name='crear_empresa'),
    path('buscar_nit/', views.BuscarNitView.as_view(), name="buscar_nit"),
    path('lista/', views.EmpresaListTemplateView.as_view(), name="listar_empresas"),
    path('scroll/', views.EmpresaListView.as_view(), name="scroll_empresas"),
    path('update/<pk>/', views.EditarEmpresaUpdateView.as_view(), name="editar_empresa"),
    path('delete/<pk>/', views.BorrarEmpresaView.as_view(), name="borrar_empresa")
]
