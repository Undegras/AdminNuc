# Generated by Django 2.2.5 on 2019-09-03 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Nucs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Nuc',
            new_name='Nucs',
        ),
        migrations.RenameModel(
            old_name='TypeOfNuc',
            new_name='TypeOfNucs',
        ),
    ]
