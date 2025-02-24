from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em') # Auto now add -> add data e hora quando o registo é criado 
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em') # Auto now -> Altera o campo sempre que alguem mexer em registros
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'


    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em') # Auto now add -> add data e hora quando o registo é criado 
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em') # Auto now -> Altera o campo sempre que alguem mexer em registros
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'



    def __str__(self):
        return self.name
    
    
class Products(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, 
                              related_name='products', verbose_name='Marca')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, 
                                 related_name='products', verbose_name='Categoria')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em') # Auto now add -> add data e hora quando o registo é criado 
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em') # Auto now -> Altera o campo sempre que alguem mexer em registros
    
    class Meta:
        ordering = ['title']
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
   
    def __str__(self):
        return self.title