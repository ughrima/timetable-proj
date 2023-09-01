# Generated by Django 4.2.4 on 2023-08-07 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_timeslot_is_booked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='booked_seats',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='is_booked',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]