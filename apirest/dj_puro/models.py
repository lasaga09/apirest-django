from django.db import models

class Categoria(models.Model):
	descripcion = models.CharField(max_length=100)
	estado = models.BooleanField(default=True)

	def __str__(self):
		return self.descripcion
	class Meta:
		verbose_name_plural = 'Categorias'
