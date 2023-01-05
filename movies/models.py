from django.db import models
import csv

class Movie(models.Model):
    id = models.CharField(max_length=256, primary_key=True)
    title_type = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    adult = models.BooleanField()
    year = models.CharField(max_length=10)
    genre = models.CharField(max_length=256)

class Person(models.Model):
    id = models.CharField(max_length=256, primary_key=True)
    name = models.CharField(max_length=256)
    birthday = models.CharField(max_length=10)
    deathday = models.CharField(max_length=10)

class PersonMovie(models.Model):
    mid = models.CharField(max_length=256)
    pid = models.CharField(max_length=256)
    order = models.IntegerField()
    category = models.CharField(max_length=256)
    job = models.CharField(max_length=256)
    chars = models.CharField(max_length=256)

