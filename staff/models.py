from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, MaxValueValidator, MinValueValidator


# Create your models here.


class Player(models.Model):
    first_name = models.CharField(blank=False, max_length=40)
    last_name = models.CharField(blank=False, max_length=40)
    national_id = models.CharField(unique=True, max_length=10,
                                   validators=[MaxLengthValidator(10), MinLengthValidator(10)],
                                   blank=False)
    age = models.IntegerField(blank=False, validators=[MaxValueValidator(100), MinValueValidator(1)])
    playing_history = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return f'{self.first_name} {self.last_name}, age = {self.age}, NID= {self.national_id}'


CERTIFICATE_CHOICES = [
    (None, '---'),
    ('D', 'D level'),
    ('C', 'C level'),
    ('B', 'B level'),
    ('A', 'A level')
]


class Coach(models.Model):
    class Meta:
        verbose_name_plural = 'Coaches'

    first_name = models.CharField(blank=False, max_length=40, validators=[MaxLengthValidator(40)])
    last_name = models.CharField(blank=False, max_length=40, validators=[MaxLengthValidator(40)])
    national_id = models.CharField(unique=True, max_length=10,
                                   validators=[MaxLengthValidator(10), MinLengthValidator(10)],
                                   blank=False)
    age = models.IntegerField(blank=False, validators=[MaxValueValidator(100), MinValueValidator(1)])
    professional_history = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    certificate = models.CharField(blank=True, null=True, max_length=1, default=None, choices=CERTIFICATE_CHOICES)

    def __str__(self):
        return f'{self.first_name} {self.last_name}, age = {self.age} , NID= {self.national_id}'
