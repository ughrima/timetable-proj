# Generated by Django 4.2.2 on 2023-07-05 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_rename_roomno_room_room_number_room_booked_by_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectname', models.CharField(max_length=100)),
            ],
        ),
    ]
