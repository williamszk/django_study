from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    return HttpResponse("<h1>This is our projects.</h1>")

def project(request, pk):
    return HttpResponse(f"<h1>This is our project {pk}.</h1>")

