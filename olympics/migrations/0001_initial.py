# Generated by Django 4.0.3 on 2022-04-01 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Olympics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.IntegerField()),
                ('season', models.CharField(choices=[('summer', 'Summer'), ('winter', 'Winter')], max_length=20)),
                ('city', models.CharField(max_length=30)),
            ],
        ),
    ]