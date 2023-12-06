from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, MaxValueValidator, MinValueValidator


# Create your models here.


class Player(models.Model):
    first_name = models.CharField(blank=False, max_length=40, validators=[MaxLengthValidator(40)])
    last_name = models.CharField(blank=False, max_length=40, validators=[MaxLengthValidator(40)])
    national_id = models.CharField(unique=True, max_length=10,
                                   validators=[MaxLengthValidator(10), MinLengthValidator(10)],
                                   blank=False)
    age = models.IntegerField(blank=False, validators=[MaxValueValidator(100), MinValueValidator(1)])
    playing_history = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return f'{self.first_name} {self.last_name}, age = {self.age}, NID= {self.national_id}'


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

    no_cert = None
    d_level = 'D'
    c_level = 'C'
    b_level = 'B'
    a_level = 'A'

    certificate = models.CharField(blank=True, null=True, max_length=1, default=no_cert, choices=[
        (no_cert, '---'),
        (d_level, 'D level'),
        (c_level, 'C level'),
        (b_level, 'B level'),
        (a_level, 'A level')
    ])

    def __str__(self):
        return f'{self.first_name} {self.last_name}, age = {self.age} , NID= {self.national_id}'
