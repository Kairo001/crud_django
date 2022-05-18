"""Modelos de la app crud"""

# Django
from django.db import models
from django.core.validators import RegexValidator

# Utilidades
from utils.models import BaseModel

class Empresa(BaseModel):
    """Modelo de Empresa."""
    nit = models.CharField('Nit de la empresa', max_length=20)
    nombre = models.CharField('Nombre de la empresa', max_length=64)
    direccion = models.CharField('Dirección de la empresa', max_length=32)
    
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{10,12}$',
        message="Número no válido."
    )

    telefono = models.CharField(validators=[phone_regex], max_length=20, blank=True)

    is_active = models.BooleanField(
        default=True,
        help_text=(
            'Designa si la empresa está o no activa. '
            'Desmarcar esto en lugar de eliminar una empresa.'
        ),
    )

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        """Unicode representation of Product."""
        return self.nombre
