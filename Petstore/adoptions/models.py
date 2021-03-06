from django.db import models

class Pet(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    name = models.CharField(max_length=80)
    submitter = models.CharField(max_length=80)
    species = models.CharField(max_length=80)
    breed = models.CharField(max_length=80, blank=True)
    description = models.TextField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    submission_date = models.DateField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=80)
