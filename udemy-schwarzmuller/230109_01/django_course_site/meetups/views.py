from django.shortcuts import render, redirect
from .models import Meetup
from .forms import RegistrationForm


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
        if request.method == "GET":
            registration_form = RegistrationForm()

        elif request.method == "POST":
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                participant = registration_form.save()
                selected_meetup.participant.add(participant)
                return redirect("confirm-registration")

        context = {
            "meetup_found": True,
            "meetup": selected_meetup,
            "form": registration_form,
        }
        return render(request, "meetups/meetup-details.html", context)

    except Exception:
        context = {"meetup_found": False}
        return render(request, "meetups/meetup-details.html", context)


def confirm_registration(request):
    context = {}
    return render(request, "meetups/registration-success.html", context)
