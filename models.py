from django.db import models


class AuthorModel(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    country = models.CharField(max_length=55)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class BookModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, null=True, blank=True)
    written_date = models.PositiveIntegerField(blank=True, null=True)
    published_date = models.PositiveIntegerField(blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.author}"

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

