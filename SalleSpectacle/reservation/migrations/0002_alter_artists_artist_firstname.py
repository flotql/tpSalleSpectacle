# Generated by Django 3.2.12 on 2022-03-23 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artists',
            name='artist_firstname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
