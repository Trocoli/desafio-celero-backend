# Generated by Django 4.0.3 on 2022-04-02 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('olympics', '0003_rename_year_olympic_year'),
        ('athletes', '0002_rename_athletes_athlete'),
        ('events', '0003_alter_event_athletes'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='olympic_game',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='olympic_game', to='olympics.olympic'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='athletes',
            field=models.ManyToManyField(related_name='athletes_in_events', to='athletes.athlete'),
        ),
    ]
