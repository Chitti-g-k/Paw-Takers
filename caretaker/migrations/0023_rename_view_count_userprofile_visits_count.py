# Generated by Django 4.2 on 2023-06-18 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caretaker', '0022_userprofile_view_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='view_count',
            new_name='visits_count',
        ),
    ]
