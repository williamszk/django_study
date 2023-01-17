from django.db import models

# Create your models here.
class Meetup(models.Model):
    title = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(unique=True)
    description = models.TextField()

