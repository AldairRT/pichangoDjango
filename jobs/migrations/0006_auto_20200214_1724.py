# Generated by Django 3.0.2 on 2020-02-14 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20200214_1633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jugador',
            old_name='nick',
            new_name='usuario',
        ),
    ]
