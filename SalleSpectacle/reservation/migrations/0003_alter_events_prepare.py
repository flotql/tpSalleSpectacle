# Generated by Django 3.2.12 on 2022-03-23 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_alter_artists_artist_firstname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='prepare',
            field=models.ManyToManyField(blank=True, to='reservation.Schedule'),
        ),
    ]
