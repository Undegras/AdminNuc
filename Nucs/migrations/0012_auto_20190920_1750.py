# Generated by Django 2.2.5 on 2019-09-20 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Nucs', '0011_auto_20190920_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nucs',
            name='ffc_code',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Nucs.FFC'),
        ),
    ]