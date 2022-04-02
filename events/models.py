from tkinter import PROJECTING
from unicodedata import name
from django.db import models

from athletes.models import Athlete
from olympics.models import Olympic
from django.db.models.deletion import PROTECT # CHANGE


class Event(models.Model): 

    event_name = models.CharField(max_length=50, blank=False, null=False)
    sport_name = models.CharField(max_length=20, blank=False, null=False)
    athletes = models.ManyToManyField(Athlete, related_name="athletes_in_events")
    olympic_game = models.ForeignKey(Olympic, related_name="olympic_game", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('event_name', 'olympic_game',) # guarantee that there's only one event entry for each olympic. 

    def __str__(self):
        return self.event_name
