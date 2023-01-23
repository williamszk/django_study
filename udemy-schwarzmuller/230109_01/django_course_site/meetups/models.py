from django.db import models


class Location(models.Model):
    """
    One location can be related to many meetups
    But one meetup can have only one location
    """

    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self) -> str:
        return f"{self.name} ({self.address})"


class Participant(models.Model):
    """
    In the relationship between meetup and participants
    It is a many to many, because a participant can be in
    subscribed to many meetups and a meetup can have many
    participants.
    """

    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.email


class Meetup(models.Model):
    title = models.CharField(max_length=200, blank=False)
    organizer_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to="images")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participant = models.ManyToManyField(Participant, blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.slug}"
