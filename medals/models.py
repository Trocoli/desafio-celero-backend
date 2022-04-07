from secrets import choice
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

    event_name = models.ForeignKey(Event, related_name= 'winners', on_delete=models.CASCADE) # chave estrangeira para evento olímpico 
    olympic_game = models.ForeignKey(Olympic, on_delete=models.CASCADE) # chave estrangeira para olimíada
    athlete = models.ManyToManyField(Athlete, related_name = 'athlete_medals') # chave estrangeira para atleta ganhador da medalha 
    medal_type = models.CharField(max_length=10, choices=MEDAL_CHOICES) # gold silver ou bronze medal 
    athlete_age = models.IntegerField(null=True) # athlete age está relacionado a medalha pois a idade presente na base de dados é a idade do atleta ao ganhar medalha 

    def __str__(self):
        if(self.athlete.name):
            return self.medal_type + ' - ' + self.athlete.name
        else:
            return self.medal_type + ' - '