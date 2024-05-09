# Generated by Django 5.0.4 on 2024-05-09 01:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playeritem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.item'),
        ),
        migrations.AlterField(
            model_name='post',
            name='sells',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.item'),
        ),
    ]
