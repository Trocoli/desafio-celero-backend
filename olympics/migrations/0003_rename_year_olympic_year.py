# Generated by Django 4.0.3 on 2022-04-02 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olympics', '0002_rename_olympics_olympic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='olympic',
            old_name='Year',
            new_name='year',
        ),
    ]
