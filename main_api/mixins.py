from rest_framework import permissions

from .permissions import IsStaffEditorPermisison 

class StaffEditorPermissionMixin():
    permissions_classes=[permissions.IsAdminUser, IsStaffEditorPermisison]

class UserQuerySetMixin():
    user_field = 'user'
    def get_queryset(self,*args, **kwargs):
        lookup_data ={}
        lookup_data[self.user_field] = self.request.user
        qs = super().get_queryset(self,*args, **kwargs)

        return qs.filter(**lookup_data)