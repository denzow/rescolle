# Generated by Django 2.0.1 on 2018-04-30 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unified_restaurant', '0005_auto_20180324_0443'),
        ('collection', '0003_auto_20180421_0239'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='collectedrestaurant',
            unique_together={('collection', 'restaurant')},
        ),
    ]
