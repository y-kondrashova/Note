from django.contrib import admin

from note_app.models import Tag, Folder, Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ["title", "folder", "last_updated_at"]
    list_filter = ["title", "tags", "folder", "last_updated_at"]
    search_fields = ["title"]


admin.site.register(Folder)
admin.site.register(Tag)
