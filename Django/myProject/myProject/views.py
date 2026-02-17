from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, this is home")

def about(request):
    return HttpResponse("Hey Buddy")