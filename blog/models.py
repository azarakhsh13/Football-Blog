from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator


# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=40, blank=False, validators=[MaxLengthValidator(40)])
    last_name = models.CharField(max_length=40, blank=False, validators=[MaxLengthValidator(40)])
    national_id = models.CharField(unique=True, max_length=10,
                                   validators=[MaxLengthValidator(10), MinLengthValidator(10)],
                                   blank=False)


class Post(models.Model):
    author = models.ManyToManyField(Author)
    to_show = models.BooleanField(blank=False, default=False)
    text = models.TextField(blank=False)
    image = models.ImageField(upload_to='Images/', blank=True)
    video = models.FileField(upload_to='Videos/', blank=True)
    date = models.DateTimeField(auto_now=True)
