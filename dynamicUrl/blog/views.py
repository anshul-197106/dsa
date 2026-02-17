from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def postDetail(request, post_id):
    return HttpResponse(f"this is post and Post id is: {post_id}")