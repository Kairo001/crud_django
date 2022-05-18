"""Vistas de la app de crud_empresa"""

# Django
from pipes import Template
from django.http import HttpResponse, JsonResponse
from django.views.generic import CreateView, View, ListView, TemplateView, UpdateView
from django.urls import reverse_lazy

# Modelos
from crud_empresa.models import Empresa

class EmpresaCreateView(CreateView):
    """Vista para crear una empresa."""
    model = Empresa
    template_name = "crear_empresa.html"
    fields = ['nit', 'nombre', 'telefono', 'direccion']
    success_url = reverse_lazy('listar_empresas')

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def form_valid(self, form):
        print("Formulario válido")
        return super().form_valid(form)

class BuscarNitView(View):
    """Vista para saber si un nit ya existe o no."""
    def get(self, request, *args, **kwargs):
        response = {}
        nit = request.GET.get('nit')

        if Empresa.objects.filter(nit=nit).exists():
            response['existe'] = True
        else:
            response['existe'] = False
        
        return JsonResponse(response)


class EmpresaListTemplateView(TemplateView):
    """Vista para listar las empresas."""
    template_name = "lista_empresas.html"

class EmpresaListView(ListView):
    """Vista para realizar scroll infinito de las empresas."""
    paginate_by = 3
    
    def get_queryset(self, *args, **kwargs):
        queryset = Empresa.objects.filter(is_active=True)
        self.object_list = queryset
        return queryset

    def get(self, *args, **kwargs):
        response = {}
        response['success'] = True
        paginator = self.get_paginator(self.get_queryset(), self.paginate_by)
        num_pages = paginator.num_pages
        page = int(self.request.GET.get('page', 1))
        if page > num_pages:
            response['success'] = False
            return JsonResponse(response)

        response['page'] = page + 1
        context_data = super().get_context_data(**kwargs)
        empresas_list = context_data['object_list']
        empresas_json_list = []
        for empresa in empresas_list:
            empresa_json = {}
            empresa_json['id'] = empresa.id
            empresa_json['nit'] = empresa.nit
            empresa_json['nombre'] = empresa.nombre
            empresa_json['telefono'] = empresa.telefono
            empresa_json['direccion'] = empresa.direccion
            empresas_json_list.append(empresa_json)
        response['empresas'] = empresas_json_list
        return JsonResponse(response)

class EditarEmpresaUpdateView(UpdateView):
    model = Empresa
    template_name = "actualzar_empresa.html"
    fields = ['nit', 'nombre', 'telefono', 'direccion']
    success_url = reverse_lazy('listar_empresas')

class BorrarEmpresaView(View):
    """Vista que cambia que cambia el estado de una empresa."""
    def post(self, request, *args, **kwargs):
        empresa = Empresa.objects.get(id=self.kwargs['pk'])
        empresa.is_active = False
        empresa.save()
        return JsonResponse({'message': '¡Empresa eliminada con éxito!'})