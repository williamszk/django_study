from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    # return HttpResponse("<h1>This is our projects.</h1>")
    context = {}
    return render(request,"projects/projects.html", context)

def project(request, pk):
    # return HttpResponse(f"<h1>This is our project {pk}.</h1>")
    context = {"pk":pk}
    return render(request, "projects/single-project.html", context)

