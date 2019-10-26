# Generated by Django 2.2.5 on 2019-09-20 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Nucs', '0010_auto_20190920_1747'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nucs',
            options={'ordering': ('fqdn_name_nuc',), 'verbose_name': 'Nuc', 'verbose_name_plural': 'Nucs'},
        ),
        migrations.AlterField(
            model_name='nucs',
            name='ffc_code',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Nucs.FFC', to_field='suff'),
        ),
    ]
