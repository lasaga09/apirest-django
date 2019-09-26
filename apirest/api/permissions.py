from rest_framework import permissions

# permisos
class IsOwner(permissions.BasePermission):
	message = 'No tiene permiso'

	def has_object_permission(self, request, view, obj):

		if request.method == permissions.SAFE_METHODS:
			return True
		return request.user == obj.owner


