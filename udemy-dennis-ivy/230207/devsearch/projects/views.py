from django.shortcuts import render, redirect
from django.http import HttpResponse

projects_list = [
    {
        "id": "1",
        "title": "Ecommerce Website",
        "description": "Fully functional ecommerce website",
    },
    {
        "id": "2",
        "title": "Portfolio Website",
        "description": "A personal website to write articles and display work",
    },
    {
        "id": "3",
        "title": "Social Network",
        "description": "An open source project built by the community",
    },
]


def projects(request):
    # return HttpResponse("<h1>This is our projects.</h1>")
    context = {"projects_list": projects_list}
    return render(request, "projects/projects.html", context)


def project(request, pk):
    # return HttpResponse(f"<h1>This is our project {pk}.</h1>")
    chosen_project_00 = filter(lambda x: x["id"] == pk, projects_list)
    if chosen_project_00 is None:
        redirect(request, "projects/project.html")
    chosen_project = list(chosen_project_00)[0]
    context = {"project": chosen_project}
    return render(request, "projects/single-project.html", context)
