from joplin_web.api.serializers import FoldersSerializer, NotesSerializer
from joplin_web.api.serializers import TagsSerializer, NoteTagsSerializer
from joplin_web.api.permissions import DjangoModelPermissions
from joplin_web.models import Folders, Notes, Tags, NoteTags


from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination

############
#
#  FOLDERS
#
############


class FoldersResultsSetPagination(PageNumberPagination):
    """
    pagination for folders
    """
    page_size = 20
    max_page_size = 50


class FoldersViewSet(viewsets.ModelViewSet):
    """
    Folders

    This viewset provides `list`, `create`, `retrieve`, `update`
    and `destroy` actions.
    """
    queryset = Folders.objects.all()
    serializer_class = FoldersSerializer
    pagination_class = FoldersResultsSetPagination
    # filter the folder
    filter_backends = (filters.OrderingFilter,)
    permission_classes = (DjangoModelPermissions, )
    ordering_fields = ('title', )
    ordering = ('title',)

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
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    pagination_class = NotesResultsSetPagination
    # filter the notes
    filter_backends = (filters.OrderingFilter,)
    permission_classes = (DjangoModelPermissions, )
    ordering_fields = ('title', )
    ordering = ('title',)


class NoteTagsViewSet(viewsets.ModelViewSet):
    """
    Note and related Tags

    This viewset provides `list`, `create`, `retrieve`, `update`
    and `destroy` actions.
    """
    queryset = NoteTags.objects.all()
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
        inner_qs = NoteTags.objects.all().values('note_id')
        # 2 - get all the notes where the note id is not in the previous NoteTags QuerySet
        return Notes.objects.exclude(id__in=inner_qs)


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
        parent_id = self.kwargs['parent_id']
        return Notes.objects.filter(parent_id=parent_id)


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
        inner_qs = NoteTags.objects.filter(tag_id=tag_id).values('note_id')
        # 2 - get all the notes where the note id is in the previous NoteTags QuerySet
        return Notes.objects.filter(id__in=inner_qs)

############
#
#  TAGS
#
############


class TagsResultsSetPagination(PageNumberPagination):
    """
    pagination for tags
    """
    page_size = 20
    max_page_size = 50


class TagsViewSet(viewsets.ModelViewSet):
    """
    Tags

    This viewset provides `list`, `create`, `retrieve`, `update`
    and `destroy` actions.
    """
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    pagination_class = TagsResultsSetPagination
    # filter the tags
    filter_backends = (filters.OrderingFilter,)
    permission_classes = (DjangoModelPermissions, )
    ordering_fields = ('title', )
    ordering = ('title',)


