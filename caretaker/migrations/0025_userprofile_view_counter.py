# Generated by Django 4.2 on 2023-06-18 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caretaker', '0024_remove_userprofile_visits_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='view_counter',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
