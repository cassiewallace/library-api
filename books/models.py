from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=125, null=False)
    author = models.CharField(max_length=125, null=False)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f'{self.title} by {self.author}'