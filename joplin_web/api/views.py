from django.core.management import call_command, CommandError
from django.db.models import Q, Count

from joplin_web.api.serializers import FoldersSerializer, NotesSerializer
from joplin_web.api.serializers import TagsSerializer, NoteTagsSerializer
from joplin_web.api.permissions import DjangoModelPermissions
from joplin_web.models import Folders, Notes, Tags, NoteTags


from logging import getLogger

from rest_framework import status, viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


logger = getLogger("joplin_web.jw")

############
#
#  FOLDERS
#
############

class FoldersViewSet(viewsets.ModelViewSet):
    """
    Folders

    This viewset provides `list`, `create`, `retrieve`, `update`
    and `destroy` actions.
    """
    queryset = Folders.objects.using('joplin').all()
    serializer_class = FoldersSerializer
    permission_classes = (DjangoModelPermissions, )
    ordering_fields = ('title', )
    ordering = ('title',)

    def get_queryset(self):
        return Folders.objects.using('joplin').annotate(nb_notes=Count("notes__id"))\
            .values('title', 'nb_notes', 'id', 'parent_id').order_by('title')

    def perform_create(self, serializer):
        # do not perform any serializer.save()
        # creating a folder will be done by call_command('mkbook')
        pass

    def create(self, request, *args, **kwargs):
        serializer = FoldersSerializer(data=request.data)
        super(FoldersViewSet, self).create(request, *args, **kwargs)
        if serializer.is_valid():
            # call the joplin wrapper to create a notebook
            message = call_command('mkbook', request.data['title'])
            # an error message
            if len(message) > 0:
                return Response({'status': message})
            # all went fine
            else:
                return Response({'status': 'notebook created'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        # do not perform any serializer.save()
        # creating a note will be done by call_command('editbook')
        pass

    def update(self, request, *args, **kwargs):
        serializer = FoldersSerializer(data=request.data)
        super(FoldersViewSet, self).create(request, *args, **kwargs)
        if serializer.is_valid():
            # call the joplin wrapper to rename a notebook
            message = call_command('editbook', request.data['id'])
            # an error message
            if len(message) > 0:
                return Response({'status': message})
            # all went fine
            else:
                return Response({'status': 'folder updated'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

############
#
#  NOTES
#
############


class NotesResultsSetPagination(PageNumberPagination):
    """
    pagination for notes
    """
    page_size = 20
    max_page_size = 50


class NotesViewSet(viewsets.ModelViewSet):
    """
    Notes

    This viewset provides `list`, `create`, `retrieve`, `update`
    and `destroy` actions.
    """
    queryset = Notes.objects.using('joplin').all()
    serializer_class = NotesSerializer
    pagination_class = NotesResultsSetPagination
    permission_classes = (DjangoModelPermissions, )
    ordering_fields = ('title', )
    ordering = ('title',)

    def perform_create(self, serializer):
        # do not perform any serializer.save()
        # creating a note will be done by call_command('mknote')
        pass

    def create(self, request, *args, **kwargs):
        folder = Folders.objects.using('joplin').get(pk=request.data['parent_id'])
        serializer = NotesSerializer(data=request.data)
        super(NotesViewSet, self).create(request, *args, **kwargs)
        if serializer.is_valid():
            # call the joplin wrapper to edit a note
            message = call_command('mknote', folder.title,
                                   request.data['body'],
                                   request.data['title'])
            # an error message
            if len(message) > 0:
                return Response({'status': message})
            # all went fine
            else:
                return Response({'status': 'note created'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        # do not perform any serializer.save()
        # creating a note will be done by call_command('editnote')
        pass

    def update(self, request, *args, **kwargs):
        # folder = Folders.objects.using('joplin').get(pk=request.data['parent'])
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid():
            # call the joplin wrapper to create a note in a notebook
            message = call_command('editnote',
                                   request.data['id'],
                                   request.data['parent'],
                                   request.data['title'],
                                   request.data['body'],
                                   request.data['is_todo'])
            # an error message
            if len(message) > 0:
                return Response({'status': message})
            # all went fine
            else:
                return Response({'status': 'note updated'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return Notes.objects.using('joplin')


class NoteTagsViewSet(viewsets.ModelViewSet):
    """
    Note and related Tags

    This viewset provides `list`, `create`, `retrieve`, `update`
    and `destroy` actions.
    """
    queryset = NoteTags.objects.using('joplin').all()
    serializer_class = NoteTagsSerializer
    pagination_class = NotesResultsSetPagination
    # filter the tags
    filter_backends = (filters.OrderingFilter,)
    permission_classes = (DjangoModelPermissions, )
    ordering_fields = ('note', )
    ordering = ('note',)


class NotesWoTagsViewSet(viewsets.ModelViewSet):
    """
    Notes without any tags

    This viewset provides `list`, `create`, `retrieve`, `update`
    and `destroy` actions.
    """
    serializer_class = NotesSerializer
    pagination_class = NotesResultsSetPagination
    # filter the tags
    filter_backends = (filters.OrderingFilter,)
    permission_classes = (DjangoModelPermissions, )
    ordering_fields = ('title', )
    ordering = ('title',)

    def get_queryset(self):
        # 1 - get all the note_id of the NoteTags models
        inner_qs = NoteTags.objects.using('joplin').all().values('note_id')
        # 2 - get all the notes where the note id is not in the previous NoteTags QuerySet
        return Notes.objects.using('joplin').exclude(id__in=inner_qs)


class NotesByFolderViewSet(viewsets.ModelViewSet):
    """
    Notes for a given folder

    This viewset provides `list`, `create`, `retrieve`, `update`
    and `destroy` actions.
    """
    serializer_class = NotesSerializer
    pagination_class = NotesResultsSetPagination
    # filter the notes
    filter_backends = (filters.OrderingFilter,)
    permission_classes = (DjangoModelPermissions, )
    ordering_fields = ('title', )
    ordering = ('title',)

    def get_queryset(self):
        folder = self.kwargs['folder']
        return Notes.objects.using('joplin').filter(parent=folder)


class NotesByTagViewSet(viewsets.ModelViewSet):
    """
    Notes for a given tags

    This viewset provides `list`, `create`, `retrieve`, `update`
    and `destroy` actions.
    """
    serializer_class = NotesSerializer
    pagination_class = NotesResultsSetPagination
    # filter the tags
    filter_backends = (filters.OrderingFilter,)
    permission_classes = (DjangoModelPermissions, )
    ordering_fields = ('title', )
    ordering = ('title',)

    def get_queryset(self):
        tag_id = self.kwargs['tag_id']
        # 1 - get all the note_id of the NoteTags models
        inner_qs = NoteTags.objects.using('joplin').filter(tag=tag_id).values('note_id')
        # 2 - get all the notes where the note id is in the previous NoteTags QuerySet
        return Notes.objects.using('joplin').filter(id__in=inner_qs)

############
#
#  TAGS
#
############


class TagsViewSet(viewsets.ModelViewSet):
    """
    Tags

    This viewset provides `list`, `create`, `retrieve`, `update`
    and `destroy` actions.
    """
    queryset = Tags.objects.using('joplin').all()
    serializer_class = TagsSerializer
    permission_classes = (DjangoModelPermissions, )
    ordering_fields = ('title', )
    ordering = ('title',)

    def get_queryset(self):
        return Tags.objects.using('joplin')\
            .annotate(nb_notes=Count("notetags__note__id"))\
            .values('title', 'nb_notes', 'id')\
            .order_by('title')

    def perform_create(self, serializer):
        # do not perform any serializer.save()
        # creating a folder will be done by call_command('mkbook')
        pass

    def create(self, request, *args, **kwargs):
        serializer = TagsSerializer(data=request.data)
        super(TagsViewSet, self).create(request, *args, **kwargs)
        if serializer.is_valid():
            # call the joplin wrapper to create a note
            message = call_command('tag', 'add', request.data['parent_id'], request.data['title'])
            # an error message
            if len(message) > 0:
                return Response({'status': message})
            # all went fine
            else:
                return Response({'status': 'note created'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
