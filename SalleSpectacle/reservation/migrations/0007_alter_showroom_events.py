# Generated by Django 3.2.12 on 2022-03-23 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_alter_showroom_tyofshowroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showroom',
            name='events',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservation.events'),
        ),
    ]
