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


urlpatterns = [
    path("", views.list_web_resources, name="list-web-resources"),  # List all web resources
    path("resource/", views.scrape_web_resources, name="scrape-web-resources"),  # Scrape web resources
    path("<int:id>/", views.web_resource_detail, name="web-resource-detail"),  # Get, update, or delete a web resource
    path("delete/<int:id>/", views.delete_web_resource, name="delete-web-resource"),  # Delete a specific web resource
]

# Endpoint	Method	Description
# /api/web-resources/	GET	Get all web resources
# /api/web-resources/<int:id>/	GET	Get specific resource
# /api/web-resources/scrape/	POST	Trigger web scraping
# /api/web-resources/delete/<int:id>/	DELETE	Delete a resource