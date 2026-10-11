from django.db import models
from django.forms.fields import IntegerField

# Create your models here.
class Book(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=200)
    year_published = IntegerField()