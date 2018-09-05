from rest_framework import permissions


class DjangoModelPermissions(permissions.BasePermission):

    perms_map = {
        'GET': [],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['joplin_web.add_folders', 'joplin_web.add_notes', 'joplin_web.add_tags'],
        'PUT': ['joplin_web.change_folders', 'joplin_web.change_notes', 'joplin_web.change_tags'],
        'PATCH': ['joplin_web.change_folders', 'joplin_web.change_notes', 'joplin_web.change_tags'],
        'DELETE': ['joplin_web.delete_folders', 'joplin_web.delete_notes', 'joplin_web.delete_tags'],
    }