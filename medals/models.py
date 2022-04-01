from secrets import choice
from tokenize import blank_re
from django.db import models
from django.forms import CharField
# foreign key imports 
from athletes.models import Athlete
from events.models import Event
from olympics.models import Olympic

class Medal(models.Model):

    MEDAL_CHOICES = (
        ("gold", "Gold"),
        ("silver", "Silver"),
        ("bronze", "Bronze")
    )

    event_name = models.ForeignKey(Event, on_delete=models.CASCADE)
    olympic_game = models.ForeignKey(Olympic, on_delete=models.CASCADE)
    athlete = models.ForeignKey(Athlete, null=True, on_delete=models.SET_NULL)
    medal_type = models.CharField(max_length=10, choices=MEDAL_CHOICES)