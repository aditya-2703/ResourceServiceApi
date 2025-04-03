import requests
from django.http import JsonResponse
from .models import GitHubRepository
from django.core.cache import cache
from datetime import datetime

def scrape_github_resources(request):
    """Scrape GitHub repositories with pre-built projects."""
    repo_urls = [
        "https://api.github.com/repos/wesbos/JavaScript30",
        "https://api.github.com/repos/TheOdinProject/curriculum",
        "https://api.github.com/repos/ryanmcdermott/clean-code-javascript",
        "https://api.github.com/repos/practical-tutorials/project-based-learning",
        "https://api.github.com/repos/MunGell/awesome-for-beginners",
        "https://api.github.com/repos/llSourcell/Learn_Machine_Learning_in_3_Months",
        "https://api.github.com/repos/leereilly/games",
        "https://api.github.com/repos/lauragift21/awesome-learning-resources",
        "https://api.github.com/repos/karan/Projects",
        "https://api.github.com/repos/kallaway/100-days-of-code",
        "https://api.github.com/repos/freeCodeCamp/freeCodeCamp",
        "https://api.github.com/repos/florinpop17/app-ideas",
        "https://api.github.com/repos/firstcontributions/first-contributions",
        "https://api.github.com/repos/aneagoie/robofriends"
    ]
    
    github_resources = []
    for url in repo_urls:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            top_tags = data.get("topics", [])[:3]  # Select only the top 3 tags
            repo, _ = GitHubRepository.objects.get_or_create(
                url=data["html_url"],
                defaults={
                    "title": data["name"],
                    "description": data.get("description", ""),
                    "stars": str(data.get("stargazers_count", "0")),
                    "forks": str(data.get("forks_count", "0")),
                    "tags": top_tags,
                }
            )
            github_resources.append({
                "title": repo.title,
                "description": repo.description,
                "stars": repo.stars,
                "forks": repo.forks,
                "url": repo.url,
                "tags": repo.tags,
                "created_at": repo.created_at,
                "updated_at": repo.updated_at
            })
    
    return JsonResponse({"message": "GitHub repositories scraped successfully", "resources": github_resources})

def list_github_resources(request):
    """Fetch all GitHub resources."""
    resources = GitHubRepository.objects.all().values()
    return JsonResponse({"resources": list(resources)})

def github_resource_detail(request, id):
    """Fetch, update, or delete a specific GitHub resource."""
    try:
        resource = GitHubRepository.objects.get(id=id)
        if request.method == "GET":
            return JsonResponse({
                "title": resource.title,
                "description": resource.description,
                "stars": resource.stars,
                "forks": resource.forks,
                "url": resource.url,
                "tags": resource.tags,
                "created_at": resource.created_at,
                "updated_at": resource.updated_at
            })
        elif request.method == "DELETE":
            resource.delete()
            return JsonResponse({"message": "Resource deleted successfully."})
        else:
            return JsonResponse({"error": "Method not allowed."}, status=405)
    except GitHubRepository.DoesNotExist:
        return JsonResponse({"error": "Resource not found."}, status=404)

def delete_github_resource(request, id):
    """Delete a GitHub resource."""
    try:
        resource = GitHubRepository.objects.get(id=id)
        resource.delete()
        return JsonResponse({"message": "Resource deleted successfully."})
    except GitHubRepository.DoesNotExist:
        return JsonResponse({"error": "Resource not found."}, status=404)