from django.shortcuts import render
from .models import Meetup


def index(request):
    meetups = Meetup.objects.all()
    context = {
        "show_meetups": True,
        "meetups": meetups,
    }
    return render(request, "meetups/index.html", context)


def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        context = {"meetup_found": True, "selected_meetup": selected_meetup}
        return render(request, "meetups/meetup-details.html", context)
    except Exception:
        context = {"meetup_found": False}
        return render(request, "meetups/meetup-details.html", context)
