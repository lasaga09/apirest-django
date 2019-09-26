from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import *



def categoria_list(request):
	MAX_OBJECTS = 20
	categoria  = Categoria.objects.all()[:MAX_OBJECTS]
	data = {"results":list(categoria.values("id","descripcion","estado"))}
	return JsonResponse(data)

def categoria_detalle(request, pk):
	categoria = get_object_or_404(Categoria, pk=pk)
	data = {
	"results":	{
				"id":categoria.id,
				"descripcion":categoria.descripcion,
				"estado":categoria.estado
				}
			}
	return JsonResponse(data)