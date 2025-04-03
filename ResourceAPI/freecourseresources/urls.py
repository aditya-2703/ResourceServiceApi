"""ResourceAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_courses, name="list-courses"),  # List all courses
    path("course/", views.create_course, name="create-course"),  # Create a course
    path("<int:id>/", views.course_detail, name="course-detail"),  # Get, update, or delete a course
    path("scrape/", views.scrape_courses, name="scrape-courses"),  # Scrape new courses
    path("delete/<int:id>/", views.delete_course, name="delete-course"),  # Delete a specific course
]



# Endpoint	Method	Description
# /api/web-resources/	GET	Get all web resources
# /api/web-resources/<int:id>/	GET	Get specific resource
# /api/web-resources/scrape/	POST	Trigger web scraping
# /api/web-resources/delete/<int:id>/	DELETE	Delete a resource