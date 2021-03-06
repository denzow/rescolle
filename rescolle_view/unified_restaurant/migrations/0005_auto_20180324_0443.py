# Generated by Django 2.0.1 on 2018-03-24 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unified_restaurant', '0004_unifiedrestaurant_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnifiedRestaurantImageUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unified_restaurant.UnifiedRestaurant')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='unifiedrestaurantimageurl',
            unique_together={('restaurant', 'image_url')},
        ),
    ]
