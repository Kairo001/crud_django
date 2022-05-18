# Django
from django.shortcuts import redirect
from django.views.generic import View

class IndexView(View):

    def dispatch(self, request, *args, **kwargs):
        return redirect('crear_empresa')