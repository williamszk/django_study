from django.db import models

# Create your models here.
class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to="images")

    def __str__(self) -> str:
        return self.slug





