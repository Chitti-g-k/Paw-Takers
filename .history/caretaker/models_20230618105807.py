from django.db import models
from django.contrib.auth.models import User

SERVICE_CHOICES = [
    ('Pet Boarding', 'Pet Boarding'),
    ('Pet Grooming', 'Pet Grooming'),
    ('Dog Training', 'Dog Training'),
    ('Pet Sitting', 'Pet Sitting'),
    ('Dog Walking', 'Dog Walking'),
    ('Dog Daycare', 'Dog Daycare'),
    ('Pet Ownership Certificate', 'Pet Ownership Certificate'),
    ('Pet Relocation', 'Pet Relocation'),
    ('Pet Sitting - Events', 'Pet Sitting - Events'),
    ('Pet Cab', 'Pet Cab'),
    ('Pet Insurance', 'Pet Insurance'),
    ('Pet Funeral', 'Pet Funeral'),
    ('Pet Nutrition', 'Pet Nutrition'),
]

class Service(models.Model):
    name = models.CharField(max_length=100, choices=SERVICE_CHOICES)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    form_number = models.CharField(max_length=12, null=True)
    phone_number = models.CharField(max_length=10, null=True)
    backup_phonenumber = models.CharField(max_length=10, null=True)
    first_line = models.CharField(max_length=100, null=True)
    second_line = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=50, null=True)
    postal_code = models.CharField(max_length=20, null=True)
    description = models.TextField(null=True)
    services_description = models.ManyToManyField(Service, through='ServiceDescription')
    image = models.ImageField(upload_to='caretaker_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class ServiceDescription(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_profile.name} - {self.service.name}"