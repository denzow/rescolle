# Generated by Django 2.0.1 on 2018-03-15 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unified_restaurant', '0002_auto_20180315_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unifiedrestaurant',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='unifiedrestaurant',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]