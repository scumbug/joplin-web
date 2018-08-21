from django.conf.urls import url, include

from joplin_web.api.views import FoldersViewSet, NotesViewSet, TagsViewSet
from joplin_web.api.views import NoteTagsViewSet, NotesWoTagsViewSet
from joplin_web.api.views import NotesByFolderViewSet, NotesByTagViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'folders', FoldersViewSet)
router.register(r'notes', NotesViewSet)
router.register(r'tags', TagsViewSet)
router.register(r'notetags', NoteTagsViewSet)
router.register(r'notes_no_tags', NotesWoTagsViewSet, base_name='notes_no_tags')

urlpatterns = [
    url(r'^', include(router.urls)),
    url('^notes/folder/(?P<parent_id>.+)', NotesByFolderViewSet.as_view({'get': 'list'})),
    url('^notes/tag/(?P<tag_id>.+)', NotesByTagViewSet.as_view({'get': 'list'})),
]