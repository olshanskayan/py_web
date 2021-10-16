from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. It's my first index.")

def home():
    return("")
