from django.shortcuts import render


def index(request):
    context = {
        "show_meetups": False,
        "meetups": [
            {"title": "A First Meetup"},
            {"title": "A Second Meetup"},
        ]
    }
    return render(request, "meetups/index.html", context)
