# Generated by Django 4.0.3 on 2022-04-04 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0003_alter_athlete_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='medals_count',
            field=models.IntegerField(default=0),
        ),
    ]
