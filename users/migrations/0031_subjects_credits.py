# Generated by Django 4.2.4 on 2023-08-29 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_delete_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='credits',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
