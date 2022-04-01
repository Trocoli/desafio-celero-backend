from tkinter import PROJECTING
from unicodedata import name
from django.db import models

from athletes.models import Athlete
from django.db.models.deletion import PROTECT # CHANGE


class Event(models.Model): 

    event_name = models.CharField(max_length=50, blank=False, null=False)
    sport_name = models.CharField(max_length=20, blank=False, null=False)
    athletes = models.ManyToManyField(Athlete, null=True)

    def __str__(self):
        return self.event_name
