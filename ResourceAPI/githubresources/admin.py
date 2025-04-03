from django.contrib import admin
from .models import GitHubRepository

@admin.register(GitHubRepository)
class GitHubRepositoryAdmin(admin.ModelAdmin):
    list_display = ("title", "stars", "forks", "url", "created_at", "updated_at")
    search_fields = ("title", "description", "url")
    list_filter = ("stars", "forks", "created_at", "updated_at")
    ordering = ("-stars", "-forks")
    readonly_fields = ("created_at", "updated_at")
