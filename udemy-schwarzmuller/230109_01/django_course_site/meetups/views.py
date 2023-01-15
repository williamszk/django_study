from django.shortcuts import render


def index(request):
    context = {
        "show_meetups": True,
        "meetups": [
            {
                "title": "A First Meetup",
                "location": "New York",
                "slug": "a-first-meetup",
            },
            {
                "title": "A Second Meetup",
                "location": "Istanbul",
                "slug": "a-second-meetup",
            },
        ],
    }
    return render(request, "meetups/index.html", context)


def meetup_details(request, meetup_slug):
    selected_meetup = {
        "title": "The meetup selected",
        "description": "This is the description of the meetup",
    }
    context = {"selected_meetup": selected_meetup}
    return render(request, "meetups/meetup-details.html", context)
