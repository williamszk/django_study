from django.shortcuts import render, redirect
from .models import Project

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
    project = Project.objects.all()
    context = {"projects_list": project}
    return render(request, "projects/projects.html", context)


def project(request, pk):
    # chosen_project_00 = filter(lambda x: x["id"] == pk, projects_list)
    # if chosen_project_00 is None:
    #     redirect(request, "projects/project.html")
    # chosen_project = list(chosen_project_00)[0]
    chosen_project = Project.objects.get(id=pk)
    if chosen_project is None:
        redirect(request, "projects/project.html")
    context = {"project": chosen_project}
    return render(request, "projects/single-project.html", context)
