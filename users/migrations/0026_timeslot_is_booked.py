# Generated by Django 4.2.2 on 2023-07-27 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_alter_timeslot_start_hour'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='is_booked',
            field=models.BooleanField(default=False),
        ),
    ]
