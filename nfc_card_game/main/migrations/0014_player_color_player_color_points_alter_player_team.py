# Generated by Django 5.0.4 on 2024-05-05 20:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0013_gamesettings_activity_card_uuid"),
    ]

    operations = [
        migrations.AddField(
            model_name="player",
            name="color",
            field=models.CharField(
                blank=True,
                choices=[
                    ("RED", "Red"),
                    ("BLUE", "Blue"),
                    ("GREEN", "Green"),
                    ("YELLOW", "Yellow"),
                ],
                default=None,
                max_length=20,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="player",
            name="color_points",
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="player",
            name="team",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="main.team",
            ),
        ),
    ]
