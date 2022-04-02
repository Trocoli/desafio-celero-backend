# Generated by Django 4.0.3 on 2022-04-02 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0002_rename_athletes_athlete'),
        ('medals', '0003_medal_medal_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medal',
            name='athlete',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='athletes.athlete'),
            preserve_default=False,
        ),
    ]
