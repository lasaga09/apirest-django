from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework import generics

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Producto, Categoria, SubCategoria
from .serializers import ProductoSerializer, CategoriaSerializer, SubCategoriaSerializer, UserSerializer

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .permissions import IsOwner

# class ProductoList(APIView):
# 	def get(self, request):
# 		prod = Producto.objects.all()[:20]
# 		data = ProductoSerializer(prod, many=True).data 
# 		return Response(data)


# class ProductoDetalle(APIView):
# 	def get(self, request, pk):
# 		prod = get_object_or_404(Producto, pk=pk)
# 		data = ProductoSerializer(prod).data 
# 		return Response(data)
# 		


# lista y crea
class ProductoList(generics.ListCreateAPIView):
	queryset = Producto.objects.all()
	serializer_class = ProductoSerializer

class ProductoDetalle(generics.RetrieveDestroyAPIView):
	queryset = Producto.objects.all()
	serializer_class = ProductoSerializer

# class CategoriaSave(generics.CreateAPIView):
# 	serializer_class = CategoriaSerializer

class CategoriaList(generics.ListCreateAPIView):
	queryset = Categoria.objects.all()
	serializer_class = CategoriaSerializer

class CategoriaDetalle(generics.RetrieveDestroyAPIView):
	queryset = Categoria.objects.all()
	serializer_class = CategoriaSerializer

class SubCategoriaList(generics.ListCreateAPIView):
	def get_queryset(self):
		queryset = SubCategoria.objects.filter(categoria=self.kwargs["pk"])
		return queryset
	serializer_class = SubCategoriaSerializer

# otra manera de add
class SubCategoriaAdd(APIView):
	def post(self, request, c_pk):
		descripcion = request.data.get("descripcion")
		data = {"categoria":c_pk, "descripcion":descripcion}
		serializer = SubCategoriaSerializer(data=data)

		if serializer.is_valid():
			sc = serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		else:
			return Response(serializer.erros, status = status.HTTP_404_BAD_REQUEST)




# otra manera es con viewset
class ProductoViewSet(viewsets.ModelViewSet):
	queryset = Producto.objects.all()
	serializer_class = ProductoSerializer
	permission_classes = ([IsAuthenticated, IsOwner])


class UserCreate(generics.CreateAPIView):
	authentication_classes = ()
	permission_classes = ()
	serializer_class = UserSerializer


# login
class Login(APIView):

	permission_classes = ()

	def post(self, request):
		username = request.data.get("username")
		password = request.data.get("password")
		user = authenticate(username=username, password=password)

		if user:
			return Response({"token":user.auth_token.key, "status":"ok"})
		else:
			return Response({"errors":"Credenciales incorrectas"}, status = status.HTTP_404_BAD_REQUEST)

