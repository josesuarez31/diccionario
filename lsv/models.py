from django.db import models
from django.core.validators import FileExtensionValidator


class Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Word(models.Model):
    word = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    video = models.FileField(upload_to='videos_uploaded',null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    numbers = models.ManyToManyField("self", blank=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.word
