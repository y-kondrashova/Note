from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from note_app.models import Note, Tag, Folder


def index(request: HttpRequest) -> HttpResponse:
    num_notes = Note.objects.count()
    num_tags = Tag.objects.count()
    num_folders = Folder.objects.count()
    context = {
        "num_notes": num_notes,
        "num_tags": num_tags,
        "num_folders": num_folders,
    }
    return render(request, "note_app/index.html", context)


def filter_by_folders(request: HttpRequest, pk: int) -> HttpResponse:
    note_list = Note.objects.select_related("folder").filter(folder_id=pk)
    folder = Folder.objects.get(pk=pk)
    context = {
        "note_list": note_list,
        "folder": folder,
    }
    return render(request, "note_app/note_list.html", context)


def filter_by_tags(request: HttpRequest, pk: int) -> HttpResponse:
    tag = Tag.objects.get(pk=pk)
    note_list = Note.objects.prefetch_related("tags").filter(tags=tag)
    context = {
        "note_list": note_list,
        "tag": tag
    }
    return render(request, "note_app/note_list.html", context)


class NoteListView(generic.ListView):
    model = Note
    queryset = Note.objects.prefetch_related("tags", "folder")
    paginate_by = 50


class FolderListView(generic.ListView):
    model = Folder


class TagListView(generic.ListView):
    model = Tag
