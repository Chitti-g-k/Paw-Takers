# Generated by Django 4.2 on 2023-06-18 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caretaker', '0017_remove_servicedescription_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(choices=[('Pet Boarding', 'Pet Boarding'), ('Pet Grooming', 'Pet Grooming'), ('Dog Training', 'Dog Training'), ('Pet Sitting', 'Pet Sitting'), ('Dog Walking', 'Dog Walking'), ('Dog Daycare', 'Dog Daycare'), ('Pet Ownership Certificate', 'Pet Ownership Certificate'), ('Pet Relocation', 'Pet Relocation'), ('Pet Sitting - Events', 'Pet Sitting - Events'), ('Pet Cab', 'Pet Cab'), ('Pet Insurance', 'Pet Insurance'), ('Pet Funeral', 'Pet Funeral'), ('Pet Nutrition', 'Pet Nutrition')], max_length=100),
        ),
    ]
