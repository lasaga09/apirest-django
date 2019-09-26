from rest_framework.routers import DefaultRouter

from django.urls import path, include
from .apiviews import ProductoList, ProductoDetalle
from .apiviews import CategoriaList, SubCategoriaList, CategoriaDetalle, SubCategoriaAdd, UserCreate, \
						Login
from .apiviews import ProductoViewSet

# obtener token login
from rest_framework.authtoken import views

# para documentacion
from rest_framework_documentation import include_docus_urls


router = DefaultRouter()
router.register("v2/productos", ProductoViewSet, base_name= 'productos')

urlpatterns = [
	path('v1/productos', ProductoList.as_view(), name='producto_list'),
	path('v1/productos/<int:pk>', ProductoDetalle.as_view(), name='producto_detalle'),
	path('v1/categorias', CategoriaList.as_view(), name='categoria_list'),
	path('v1/categorias/<int:pk>', CategoriaDetalle.as_view(), name='categoria_detalle'),
	path('v1/categorias/<int:pk>/subcategorias/', SubCategoriaList.as_view(), name='subcategoria_list'),
	path('v1/usuarios', UserCreate.as_view(), name='usuario_create'),

	path('v1/categorias/<int:c_pk>/scadd/', SubCategoriaAdd.as_view(), name='subcategoria_add'),

	path('v1/login/', Login.as_view(), name='login'),

	path('v1/login-drf/', views.obtain_auth_token, name='login_drf'),

	path('coreapi/', include_docus_urls(title="Documentacion coreapi")),


]


# para routers de viewsets
urlpatterns += router.urls