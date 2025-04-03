from django.db import models
import random

def generate_random_rating():
    return round(random.uniform(3.0, 5.0), 1)

class FreeCourseResource(models.Model):
    class Meta:
        db_table = "free_course_resources"
        verbose_name = "Free Course Resource"
        verbose_name_plural = "Free Course Resources"

    course_source = models.CharField(max_length=100, null=False)  # Now just a string
    title = models.CharField(max_length=255, null=False)
    instructor = models.CharField(max_length=255, blank=True, null=True)
    rating = models.FloatField(default=generate_random_rating)  # Using a named function instead of lambda
    course_link = models.URLField(unique=True, null=False)
    image_url = models.URLField(default="https://example.com/default-course-image.jpg")  # Default image

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.course_source}"