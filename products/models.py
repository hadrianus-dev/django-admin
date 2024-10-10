from venv import create
from django.db import models
from uuid import uuid4

# Create your models here.

class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True, verbose_name='Marca')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    is_active = models.BooleanField(default=False, verbose_name='Ativo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ["created_at", "name"]

    def __str__(self):
        return self.name
    
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True, verbose_name='Categória')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    is_active = models.BooleanField(default=False, verbose_name='Ativo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Categória'
        verbose_name_plural = 'Categórias'
        ordering = ["created_at", "name"]

    def __str__(self):
        return self.name
    
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True, verbose_name='Produto')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')

    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='Marca')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Categoria')

    is_active = models.BooleanField(default=False, verbose_name='Ativo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ["created_at", "name"]

    def __str__(self):
        return self.name
