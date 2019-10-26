# Generated by Django 2.2.5 on 2019-09-20 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Nucs', '0019_auto_20190920_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='nucs',
            name='ffc_code',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Nucs.FFC', to_field='suff'),
        ),
        migrations.AlterField(
            model_name='ffc',
            name='suff',
            field=models.CharField(max_length=6, unique=True),
        ),
    ]
