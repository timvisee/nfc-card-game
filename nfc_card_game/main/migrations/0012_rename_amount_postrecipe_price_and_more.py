# Generated by Django 5.0.4 on 2024-05-09 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_post_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postrecipe',
            old_name='amount',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='postrecipe',
            name='required',
        ),
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('RESOURCE', 'Resource'), ('MINER', 'Miner')]),
        ),
    ]