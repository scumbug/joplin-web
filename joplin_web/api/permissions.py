from rest_framework import permissions


class DjangoModelPermissions(permissions.BasePermission):

    perms_map = {
        'GET': [],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['joplin_web.add', 'joplin_web.add'],
        'PUT': ['joplin_web.change', 'joplin_web.change'],
        'DELETE': ['joplin_web.delete', 'joplin_web.delete'],
    }