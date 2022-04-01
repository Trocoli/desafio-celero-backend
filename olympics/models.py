from django.db import models

class Olympic(models.Model):

    SEASON_CHOICS = (
        ("summer", "Summer"),
        ("winter", "Winter")
    )

    year = models.IntegerField()
    season = models.CharField(max_length=20, choices=SEASON_CHOICS, blank=False, null=False )
    city = models.CharField(max_length=30, blank=False, null=False )

    def __str__(self):
        return self.city + '_' + str(self.year)