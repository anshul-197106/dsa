from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, this is UK")

def about(request):
    return HttpResponse("Hey Buds")