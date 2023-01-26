from django.shortcuts import render, redirect
from .models import Meetup, Participant
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
                # participant = registration_form.save()
                user_email = registration_form.cleaned_data["email"]
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participant.add(participant)
                return redirect("confirm-registration", meetup_slug=meetup_slug)

        context = {
            "meetup_found": True,
            "meetup": selected_meetup,
            "form": registration_form,
        }
        return render(request, "meetups/meetup-details.html", context)

    except Exception:
        context = {"meetup_found": False}
        return render(request, "meetups/meetup-details.html", context)


def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    context = {"organizer_email":meetup.organizer_email}
    return render(request, "meetups/registration-success.html", context)
