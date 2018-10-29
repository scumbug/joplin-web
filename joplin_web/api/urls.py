from django.conf.urls import url, include

from joplin_web.api.views import FoldersViewSet, NotesViewSet, TagsViewSet, TasksViewSet
from joplin_web.api.views import NotesByFolderViewSet, NotesByTagViewSet, VersionViewSet, NoteTagsByNoteIdViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'folders', FoldersViewSet)
router.register(r'notes', NotesViewSet)
router.register(r'tasks', TasksViewSet, base_name='tasks')
router.register(r'tags', TagsViewSet)
router.register(r'version', VersionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url('^notes/folder/(?P<folder>.+)', NotesByFolderViewSet.as_view({'get': 'list'})),
    url('^notes/tag/(?P<tag_id>.+)', NotesByTagViewSet.as_view({'get': 'list'})),
    url('^notetags/(?P<note_id>.+)', NoteTagsByNoteIdViewSet.as_view({'get': 'list'}))
]
