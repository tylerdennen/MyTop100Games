from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    name = models.CharField(max_length=254, db_index=True)
    slug = models.SlugField(unique=True)
    image = models.URLField(null=True)
    date_released = models.DateField(null=True)
    genres = models.ManyToManyField('Genre', related_name='games', blank=True)
    platforms = models.ManyToManyField('Platform', related_name='games', blank=True)
    users = models.ManyToManyField(User, related_name='games', blank=True, through='PositionInTop')


class Genre(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(unique=True)


class Platform(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(unique=True)


class PositionInTop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    position = models.IntegerField()
