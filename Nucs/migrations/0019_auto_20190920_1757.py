# Generated by Django 2.2.5 on 2019-09-20 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nucs', '0018_remove_nucs_ffc_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ffc',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
