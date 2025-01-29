from rest_framework import permissions

from .permissions import IsStaffEditorPermisison 

class StaffEditorPermissionMixin():
    permissions_classes=[permissions.IsAdminUser, IsStaffEditorPermisison]