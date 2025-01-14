# Generated by Django 5.0.4 on 2024-05-10 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_auto_20240509_2152"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="name",
            field=models.CharField(
                choices=[
                    ("BIJL", "Bijl"),
                    ("TANDWIEL", "Tandwiel"),
                    ("RUPSBAND", "Rupsband"),
                    ("BLAUW", "Blauw"),
                    ("GROEN", "Groen"),
                    ("ROOD", "Rood"),
                    ("MIJNWERKER", "Mijnwerker"),
                    ("DRILBOOR", "Drilboor"),
                    ("BULLDOZER", "Bulldozer"),
                ]
            ),
        ),
    ]
