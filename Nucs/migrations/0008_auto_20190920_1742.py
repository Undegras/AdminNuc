# Generated by Django 2.2.5 on 2019-09-20 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Nucs', '0007_nucs_ffc_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nucs',
            name='ffc_code',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Nucs.FFC'),
        ),
    ]
