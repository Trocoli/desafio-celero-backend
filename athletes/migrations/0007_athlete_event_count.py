# Generated by Django 4.0.3 on 2022-04-06 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0006_remove_athlete_events_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='event_count',
            field=models.IntegerField(default=0),
        ),
    ]