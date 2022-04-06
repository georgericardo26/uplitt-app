from rest_framework.permissions import BasePermission

# class IsOwnerVirtualShop(BasePermission):
#     def has_permission(self, request, view):
#         user = request.user


class CheckIdIsSeller(BasePermission):
    """
    Allows access only to authenticated users.
    """

    # def has_permission(self, request, view):
    #     """
    #     Return `True` if permission is granted, `False` otherwise.
    #     """
    #     return True

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """

        if obj.seller.pk == request.user.pk:
            return True
        return False
