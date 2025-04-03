from django.db import models

class GitHubRepository(models.Model):
    class Meta:
        db_table = "github_repositories"  # Explicit table name

    title = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True, null=True)
    stars = models.CharField(max_length=50, blank=True, null=True)
    forks = models.CharField(max_length=50, blank=True, null=True)
    url = models.URLField(unique=True, null=False)
    tags = models.JSONField(default=list, blank=True)  # Storing list of tags
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
