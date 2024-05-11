# Generated by Django 5.0.4 on 2024-05-11 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('Blauw', '🔵'), ('Groen', '🟢'), ('Rood', '🔴')]),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(choices=[('BIJL', 'Bijl'), ('TANDWIEL', 'Tandwiel'), ('RUPSBAND', 'Rupsband'), ('Blauw', '🔵'), ('Groen', '🟢'), ('Rood', '🔴'), ('MIJNWERKER', 'Mijnwerker'), ('DRILBOOR', 'Drilboor'), ('BULLDOZER', 'Bulldozer')]),
        ),
        migrations.AlterField(
            model_name='mine',
            name='currency',
            field=models.CharField(choices=[('Blauw', '🔵'), ('Groen', '🟢'), ('Rood', '🔴')], max_length=100),
        ),
        migrations.AlterField(
            model_name='mine',
            name='name',
            field=models.CharField(choices=[('Blauw', '🔵'), ('Groen', '🟢'), ('Rood', '🔴')], max_length=100),
        ),
    ]