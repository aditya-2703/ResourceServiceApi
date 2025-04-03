from django.contrib import admin
from .models import Resource

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ("title", "resource_type", "link", "project_id", "created_at", "last_modified_at")
    search_fields = ("title", "resource_type", "link")
    list_filter = ("resource_type", "created_at", "last_modified_at")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "last_modified_at")
