from django.contrib import admin
from django.urls import path, include

#Vistas
from config import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view()),
    path('empresa/', include('crud_empresa.urls'))
]
