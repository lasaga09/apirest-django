from django.db import models
from django.conf import settings

class OwnerModel(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	class Meta:
		abstract = True
		# abstract para que no tome en cuenta djanog

class Categoria(OwnerModel):
	descripcion = models.CharField(max_length=100, help_text='descripcion de la categoria', unique=True)

	def __str__(self):
		return '{}'.format(self.descripcion)

	class Meta:
		verbose_name_plural = 'Categorias'

class SubCategoria(OwnerModel):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Sub Categoría'
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion,self.descripcion)

    class Meta:
        verbose_name_plural = "Sub Categorías"
        unique_together = ('categoria','descripcion')

class Producto(OwnerModel):
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción del Producto',
        unique=True
    )
    fecha_creado = models.DateTimeField()
    vendido = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.descripcion)

    class Meta:
        verbose_name_plural = "Productos"


