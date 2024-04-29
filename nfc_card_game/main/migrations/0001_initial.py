# Generated by Django 5.0.3 on 2024-04-01 10:26

import django.db.models.deletion
import nfc_card_game.main.models.player
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Mine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "currency",
                    models.CharField(
                        choices=[
                            ("BLUE", "Blauwe munt"),
                            ("RED ", "Rode munt"),
                            ("GREEN", "Groene munt"),
                        ]
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "card_uuid",
                    models.CharField(
                        default=nfc_card_game.main.models.player.short_uuid,
                        max_length=10,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("buys", models.JSONField(default=dict)),
                ("sells", models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "card_uuid",
                    models.CharField(
                        default=nfc_card_game.main.models.player.short_uuid,
                        max_length=10,
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100)),
                (
                    "section",
                    models.CharField(
                        choices=[
                            ("OBV", "Ochtendbevers"),
                            ("MBV", "Middagbevers"),
                            ("MAL", "Malicetehorde"),
                            ("SJH", "Sint Jorishorde"),
                            ("COM", "Commoosiehorde"),
                            ("STH", "Sterrenhorde"),
                            ("DOB", "Donkerblauwe troep"),
                            ("SJV", "Sint Jorisvendel"),
                            ("LIB", "Lichtblauwe troep"),
                            ("STV", "Sterrenvendel"),
                            ("EXP", "Explorers"),
                            ("STAF", "Leiding"),
                            ("", "Not set"),
                        ],
                        default="",
                        max_length=4,
                    ),
                ),
                ("inventory", models.JSONField(default=dict)),
                (
                    "team",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="main.team",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TeamMine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("inventory", models.JSONField(default=dict)),
                (
                    "mine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.mine"
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.team"
                    ),
                ),
            ],
        ),
    ]
