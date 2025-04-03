from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")

def add(request):
    num1 = int(request.GET['num1'])
    num2 = int(request.GET['num2'])
    res = num1 + num2