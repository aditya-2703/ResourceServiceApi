import requests
from bs4 import BeautifulSoup
import random
import json
# import redis
from django.http import JsonResponse
from .models import FreeCourseResource
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

# Comment out Redis connection
# redis_client = redis.StrictRedis(host="127.0.0.1", port=6379, db=1, decode_responses=True)

CACHE_KEY = "scraped_courses"
CACHE_TIMEOUT = 3600  # 1 hour

# Helper function to generate a random rating
def generate_random_rating():
    return round(random.uniform(3.0, 5.0), 1)

def scrape_courses(request):
    """Scrape free courses from Class Central with Django's cache."""

    # 1️⃣ **Check Django Cache instead of Redis**
    cached_data = cache.get(CACHE_KEY)
    if cached_data:
        return JsonResponse({
            "message": "Returned from Django Cache ✅",
            "scraped_courses": json.loads(cached_data)
        })

    url = "https://www.classcentral.com/search?q=free+courses&free=true"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return JsonResponse({"error": f"Failed to fetch data, status {response.status_code}"}, status=500)

        soup = BeautifulSoup(response.text, "html.parser")
        course_elements = soup.select(".course-name")  # Adjust selector based on site structure
        scraped_courses = []
        new_courses_added = 0

        for course in course_elements:
            title = course.text.strip()
            link = "https://www.classcentral.com" + course.get("href", "#")

            # Extract course source (Coursera, Udemy, etc.)
            source_element = course.find_previous("span", class_="provider")
            course_source = source_element.text.strip() if source_element else "Unknown"

            # Extract instructor if available
            instructor_element = course.find_next("span", class_="instructor")
            instructor = instructor_element.text.strip() if instructor_element else None

            # Extract image if available
            image_element = course.find_previous("img")
            image_url = image_element["src"] if image_element else "https://example.com/default-course-image.jpg"

            # Generate rating
            rating = generate_random_rating()

            # Check if course already exists in DB
            course_obj, created = FreeCourseResource.objects.get_or_create(
                course_link=link,
                defaults={
                    "course_source": course_source,
                    "title": title,
                    "instructor": instructor,
                    "rating": rating,
                    "image_url": image_url
                }
            )

            if created:
                new_courses_added += 1

            # Store data for response
            scraped_courses.append({
                "course_source": course_obj.course_source,
                "title": course_obj.title,
                "instructor": course_obj.instructor,
                "rating": course_obj.rating,
                "course_link": course_obj.course_link,
                "image_url": course_obj.image_url
            })

        # 2️⃣ **Store in Django Cache instead of Redis**
        cache.set(CACHE_KEY, json.dumps(scraped_courses), CACHE_TIMEOUT)

        return JsonResponse({
            "message": f"Scraping completed. {new_courses_added} new courses added. ✅",
            "scraped_courses": scraped_courses
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def list_courses(request):
    """Fetch all free course resources."""
    courses = FreeCourseResource.objects.all().values()
    return JsonResponse({"courses": list(courses)}, safe=False)

@csrf_exempt
def create_course(request):
    """Create a new course resource."""
    if request.method == "POST":
        data = json.loads(request.body)
        course, created = FreeCourseResource.objects.get_or_create(
            title=data.get("title"),
            defaults={
                "course_source": data.get("course_source", "Unknown"),
                "instructor": data.get("instructor"),
                "rating": data.get("rating"),
                "course_link": data.get("course_link"),
                "image_url": data.get("image_url"),
            },
        )
        message = "Course created successfully!" if created else "Course already exists!"
        return JsonResponse({"message": message, "course_id": course.id})

def course_detail(request, id):
    """Fetch, update, or delete a specific course resource."""
    course = get_object_or_404(FreeCourseResource, id=id)

    if request.method == "GET":
        return JsonResponse({
            "id": course.id,
            "course_source": course.course_source,
            "title": course.title,
            "instructor": course.instructor,
            "rating": course.rating,
            "course_link": course.course_link,
            "image_url": course.image_url,
        })

    if request.method == "PATCH":
        data = json.loads(request.body)
        course.course_source = data.get("course_source", course.course_source)
        course.title = data.get("title", course.title)
        course.instructor = data.get("instructor", course.instructor)
        course.rating = data.get("rating", course.rating)
        course.course_link = data.get("course_link", course.course_link)
        course.image_url = data.get("image_url", course.image_url)
        course.save()
        return JsonResponse({"message": "Course updated successfully!"})

    if request.method == "DELETE":
        course.delete()
        return JsonResponse({"message": "Course deleted successfully!"})


@csrf_exempt
def delete_course(request, id):
    """Delete a course resource."""
    course = get_object_or_404(FreeCourseResource, id=id)
    course.delete()
    return JsonResponse({"message": "Course deleted successfully!"})