from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=125, blank=False)
    author = models.CharField(max_length=125, blank=False)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE,  
        related_name='created_books', blank=True)
    checked_out_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL,
        related_name='checked_out_books', null=True, blank=True)
    cover_image = models.ImageField(blank=True, upload_to='books/images')

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} by {self.author}'
