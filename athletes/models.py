
from django.db import models
from django.db.models.deletion import PROTECT


# Create your models here.
class Athlete(models.Model):

    SEX_CHOICES = (
        ("F", "Female"),
        ("M", "Male")
    )

    name = models.CharField(max_length=200, blank=False, null = False)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    team = models.CharField(max_length=15, blank=False, null=False)
    medals_count = models.IntegerField(default=0)
    event_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
