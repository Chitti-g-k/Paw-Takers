# Generated by Django 4.1.3 on 2023-05-08 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("caretaker", "0003_remove_userprofile_author_remove_userprofile_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="image",
            field=models.ImageField(
                blank="true", null=True, upload_to="caretaker_images"
            ),
        ),
    ]
