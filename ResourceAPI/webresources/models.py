from django.db import models

class Resource(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    link = models.URLField(null=False, blank=False)
    
    resource_type = models.CharField(
        max_length=50,  
        null=True,  # Type is optional
        blank=True  # Can be left empty
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    
    project_id = models.BigIntegerField(null=False, blank=False)

    class Meta:
        db_table = "resources"
    
    def __str__(self):
        return f"{self.title} ({self.resource_type if self.resource_type else 'No Type'})"
