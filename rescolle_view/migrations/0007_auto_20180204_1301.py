# Generated by Django 2.0.1 on 2018-02-04 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rescolle_view', '0006_crawlrawdata_serial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crawlrawdata',
            name='serial',
            field=models.TextField(blank=True, null=True, unique=True),
        ),
    ]