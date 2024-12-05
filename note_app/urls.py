from django.urls import path

from note_app.views import (
    index,
    filter_by_folders,
    filter_by_tags,
    NoteListView,
    FolderListView,
    TagListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("notes/", NoteListView.as_view(), name="note-list"),
    path("folders/", FolderListView.as_view(), name="folder-list"),
    path("folders/<int:pk>/", filter_by_folders, name="folder-filter"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/<int:pk>/", filter_by_tags, name="tag-filter"),
]

app_name = "note"
