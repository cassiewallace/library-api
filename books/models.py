from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=125, null=False)
    author = models.CharField(max_length=125, null=False)
    creator = models.ForeignKey('auth.User', on_delete=models.CASCADE,  
        related_name='created_books')
    checked_out_by = models.ForeignKey('auth.User', on_delete=models.PROTECT,
        related_name='checked_out_books', null=True)

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} by {self.author}'