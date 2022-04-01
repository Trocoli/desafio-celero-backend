# Generated by Django 4.0.3 on 2022-04-01 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('athletes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('sport_name', models.CharField(max_length=20)),
                ('athletes', models.ManyToManyField(to='athletes.athletes')),
            ],
        ),
    ]