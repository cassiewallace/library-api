from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f'{self.title} by {self.author}'