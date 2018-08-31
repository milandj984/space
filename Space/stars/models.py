from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Group(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Ovo je owner - creator
    title = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True) # Ime grupe sve mala slova i umesto 'space' je '-' - koristi se za url link da pise ime a ne ID objekta
    description = models.CharField(max_length=300)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class User_Groups(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


class Pictures(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='space_upload')

    def __str__(self):
        return self.user