from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def shopList(request):
    return HttpResponse("This is a shop list page...")
def shopDetail(request):
    return HttpResponse("This is a shop detail page...")

