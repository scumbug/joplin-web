from django.conf import settings
from django.db.models import Q, Count

from joplin_api import JoplinApi
from joplin_web.api.serializers import FoldersSerializer, NotesSerializer
from joplin_web.api.serializers import TagsSerializer, VersionSerializer, NoteTagsByNoteIdSerializer
from joplin_web.api.permissions import DjangoModelPermissions
from joplin_web.models import Folders, Notes, Tags, NoteTags, Version

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
                  .values('title', 'nb_notes', 'id', 'parent_id').order_by('parent_id', 'title')
         """
         return Folders.objects.using('joplin').raw('''
         WITH RECURSIVE parent(n) AS (
         SELECT folders.id FROM folders UNION SELECT title FROM folders, parent WHERE folders.parent_id=parent.n
         )
         SELECT "folders"."title", "folders"."id", "folders"."parent_id", COUNT("notes"."id") AS "nb_notes"
         FROM "folders"
         LEFT OUTER JOIN "notes" ON ("folders"."id" = "notes"."parent_id")
         WHERE "folders"."id" IN parent
         GROUP BY "folders"."id", "folders"."title"
         ORDER BY "folders"."parent_id", "folders"."title" ASC
         ''')
         """

    def create(self, request, *args, **kwargs):
        serializer = FoldersSerializer(data=request.data)
        if serializer.is_valid():
            joplin = JoplinApi(api_type=settings.JOPLIN_API_TYPE, token=settings.JOPLIN_TOKEN)
            res = joplin.create_folder(request.data['title'])
            if res.status_code == 200:
                return Response({'status folder created'})
            return Response({'status': 'folder not created {}'.format(res.status_code)})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        serializer = FoldersSerializer(data=request.data)
        if serializer.is_valid():
            joplin = JoplinApi(api_type=settings.JOPLIN_API_TYPE, token=settings.JOPLIN_TOKEN)
            res = joplin.update_folder(request.data['id'], request.data['title'])
            if res.status_code == 200:
                return Response({'status folder updated'})
            return Response({'status': 'folder not updated {}'.format(res.status_code)})
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
    max_page_size = 20


class TasksViewSet(viewsets.ModelViewSet):
    """
    Tasks

    This viewset provides `list`, `create`, `retrieve`, `update`
    and `destroy` actions.
    """
    queryset = Notes.objects.using('joplin').all()
    serializer_class = NotesSerializer
    pagination_class = NotesResultsSetPagination
    permission_classes = (DjangoModelPermissions, )
    ordering_fields = ('title', )
    ordering = ('title',)

    def get_queryset(self):
        return Notes.objects.using('joplin').filter(todo_completed=0,
                                                    todo_due__gt=0).order_by('-is_todo', '-created_time', 'title')


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

    def get_queryset(self):
        return Notes.objects.using('joplin').order_by('created_time', 'title')

    def create(self, request, *args, **kwargs):
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid():
            data = {'is_todo': request.data.get('is_todo', 0),
                    'tags': request.data.get('tag', '')}
            joplin = JoplinApi(api_type=settings.JOPLIN_API_TYPE, token=settings.JOPLIN_TOKEN)

            res = joplin.create_note(title=request.data['title'],
                                     body=request.data['body'],
                                     parent_id=request.data['parent_id'],
                                     **data)
            if res.status_code == 200:
                return Response({'status': 'note created'})
            return Response({'status': 'note not created {}'.format(res.status_code)})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        note_id = request.data['id']
        # drop the id to pass validator
        del (request.data['id'])
        serializer = NotesSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            data = {'is_todo': request.data.get('is_todo', 0),
                    'tags': request.data.get('tag', '')}
            joplin = JoplinApi(api_type=settings.JOPLIN_API_TYPE, token=settings.JOPLIN_TOKEN)
            res = joplin.update_note(note_id=note_id,
                                     parent_id=request.data['parent_id'],
                                     title=request.data['title'],
                                     body=request.data['body'],
                                     **data)
            if res.status_code == 200:
                return Response({'status': 'note updated'})
            return Response({'status': 'note not updated {}'.format(res.status_code)})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class NoteTagsByNoteIdViewSet(viewsets.ModelViewSet):
    """
    Note and related Tags

    This viewset provides `list`, `create`, `retrieve`, `update`
    and `destroy` actions.
    """
    queryset = NoteTags.objects.using('joplin').all()
    serializer_class = NoteTagsByNoteIdSerializer
    pagination_class = NotesResultsSetPagination
    # filter the tags
    filter_backends = (filters.OrderingFilter,)
    permission_classes = (DjangoModelPermissions, )

    def get_queryset(self):
        return NoteTags.objects.using('joplin').filter(note=self.kwargs['note_id'])


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

    def create(self, request, *args, **kwargs):
        request.data['nb_notes'] = 0
        serializer = TagsSerializer(data=request.data)
        if serializer.is_valid():
            # call the joplin wrapper to create a tag
            joplin = JoplinApi(api_type=settings.JOPLIN_API_TYPE, token=settings.JOPLIN_TOKEN)
            res = joplin.create_tag(title=request.data['title'])
            if res.status_code == 200:
                return Response({'status': 'tag created'})
            return Response({'status': 'tag not created {}'.format(res.status_code)})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class VersionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Joplin version

    This viewset show the version
    """
    queryset = Version.objects.using('joplin').all()
    serializer_class = VersionSerializer
