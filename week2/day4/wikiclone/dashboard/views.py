from django.shortcuts import render
from django.http import HttpResponse
from .models import topic


def index(request):
    return HttpResponse("Hello, world. You're at the wiki index.")

def detail(request, slug):
    return HttpResponse("topic:"%topic_name)