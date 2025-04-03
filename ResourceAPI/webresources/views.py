import requests
from django.http import JsonResponse
from .models import Resource
from django.core.cache import cache
from datetime import datetime

def scrape_web_resources(request):
    """Scrape web resource data from external sources."""
    cache_key = "web_resources"
    cached_data = cache.get(cache_key)
    
    if cached_data:
        return JsonResponse({"message": "Returned from Cache ✅", "resources": cached_data})
    
    resources = [
        {"title": "Unsplash Free Images", "link": "https://unsplash.com/", "resource_type": "images"},
        {"title": "Pexels Free Videos", "link": "https://www.pexels.com/videos/", "resource_type": "videos"},
        {"title": "Giphy Animated GIFs", "link": "https://giphy.com/", "resource_type": "gifs"},
        {"title": "Flaticon Free Icons", "link": "https://www.flaticon.com/", "resource_type": "icons"},
        {"title": "FontAwesome Icons", "link": "https://fontawesome.com/", "resource_type": "icons"},
        {"title": "Google Fonts", "link": "https://fonts.google.com/", "resource_type": "fonts"},
        {"title": "Color Hunt Palettes", "link": "https://colorhunt.co/", "resource_type": "color_palette"},
        {"title": "UIGradients", "link": "https://uigradients.com/", "resource_type": "gradients"},
        {"title": "Free Sound Effects", "link": "https://freesound.org/", "resource_type": "sound"},
        {"title": "Lottie Animations", "link": "https://lottiefiles.com/", "resource_type": "animations"},
        {"title": "Bootstrap Templates", "link": "https://startbootstrap.com/", "resource_type": "templates"},
        {"title": "Creative Market Free Goods", "link": "https://creativemarket.com/free-goods", "resource_type": "design_assets"},
        {"title": "Dribbble Free UI Kits", "link": "https://dribbble.com/tags/free_ui_kit", "resource_type": "ui_components"},
        {"title": "CSS Tricks Snippets", "link": "https://css-tricks.com/snippets/css/", "resource_type": "css_snippets"}
    ]
    
    # Save to Database (Avoid Duplicates)
    for res in resources:
        if not Resource.objects.filter(link=res["link"]).exists():
            Resource.objects.create(
                title=res["title"],
                link=res["link"],
                resource_type=res["resource_type"],
                project_id=0,  # Default project ID
                created_at=datetime.now(),
                last_modified_at=datetime.now()
            )
    
    cache.set(cache_key, resources, timeout=86400)  # Cache for 24 hours
    
    return JsonResponse({"message": "Fresh Data ✅", "resources": resources})

def list_web_resources(request):
    """Fetch all web resources."""
    resources = list(Resource.objects.values())
    return JsonResponse({"resources": resources})

def web_resource_detail(request, id):
    """Fetch, update, or delete a specific web resource."""
    try:
        resource = Resource.objects.get(id=id)
        if request.method == "GET":
            return JsonResponse({"resource": {
                "id": resource.id,
                "title": resource.title,
                "link": resource.link,
                "resource_type": resource.resource_type,
                "created_at": resource.created_at,
                "last_modified_at": resource.last_modified_at,
                "project_id": resource.project_id
            }})
        elif request.method == "PUT":
            data = request.POST
            resource.title = data.get("title", resource.title)
            resource.link = data.get("link", resource.link)
            resource.resource_type = data.get("resource_type", resource.resource_type)
            resource.save()
            return JsonResponse({"message": "Resource updated successfully."})
        elif request.method == "DELETE":
            resource.delete()
            return JsonResponse({"message": "Resource deleted successfully."})
    except Resource.DoesNotExist:
        return JsonResponse({"error": "Resource not found."}, status=404)

def delete_web_resource(request, id):
    """Delete a web resource."""
    try:
        resource = Resource.objects.get(id=id)
        resource.delete()
        return JsonResponse({"message": "Resource deleted successfully."})
    except Resource.DoesNotExist:
        return JsonResponse({"error": "Resource not found."}, status=404)
