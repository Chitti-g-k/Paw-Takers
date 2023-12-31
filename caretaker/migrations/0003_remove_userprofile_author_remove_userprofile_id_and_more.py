# Generated by Django 4.1.3 on 2023-05-06 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("caretaker", "0002_userprofile_author"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="author",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="id",
        ),
        migrations.AddField(
            model_name="userprofile",
            name="user",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                related_name="profile",
                serialize=False,
                to=settings.AUTH_USER_MODEL,
                verbose_name="user",
            ),
            preserve_default=False,
        ),
    ]
