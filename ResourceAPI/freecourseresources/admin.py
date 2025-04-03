from django.contrib import admin
from .models import FreeCourseResource

@admin.register(FreeCourseResource)
class FreeCourseResourceAdmin(admin.ModelAdmin):
    list_display = ("title", "course_source", "instructor", "rating")
