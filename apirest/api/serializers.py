from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Producto, Categoria, SubCategoria


class ProductoSerializer(serializers.ModelSerializer):
	# para que guarde el owner detecta el usuario logeado
	owner = serializers.HiddenField(default = serializers.CurrentUserDefault())
	class Meta:
		model = Producto
		fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
	# para que guarde el owner detecta el usuario logeado
	owner = serializers.HiddenField(default = serializers.CurrentUserDefault())
	class Meta:
		model = Categoria
		fields = '__all__'


class SubCategoriaSerializer(serializers.ModelSerializer):
	# para que guarde el owner detecta el usuario logeado
	owner = serializers.HiddenField(default = serializers.CurrentUserDefault())
	class Meta:
		model = SubCategoria
		fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username','password','email')
		extra_kwargs = {'password':{'write_only':True}}


	def create(self, validate_data):
		user = User(
				email = validate_data["email"],
				username = validate_data["username"]
			)

		user.set_password(validate_data["password"])
		user.save()
		Token.objects.create(user=user)
		return user

