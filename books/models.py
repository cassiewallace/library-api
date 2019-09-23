from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=125, null=False)
    author = models.CharField(max_length=125, null=False)
    creator = models.ForeignKey('auth.User', related_name='books', 
        on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} by {self.author}'