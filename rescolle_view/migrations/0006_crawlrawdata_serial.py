# Generated by Django 2.0.1 on 2018-02-04 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rescolle_view', '0005_crawlrawdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='crawlrawdata',
            name='serial',
            field=models.TextField(default='empty'),
            preserve_default=False,
        ),
    ]
