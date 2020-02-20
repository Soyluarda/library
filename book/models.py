from django.db import models
from django_countries.fields import CountryField

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    country = CountryField(null=True, blank=True)
    author_pic = models.ImageField(upload_to='author', null=True, blank=True)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='publisher', null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):

    TYPE_CHOICES = [
        ("Roman", "Roman"),
        ("Edebiyat", "Edebiyat"),
        ("Felsefe", "Felsefe"),
        ("Psikoloji", "Psikoloji"),
        ("Araştırma", "Araştırma")
    ]

    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author,blank=True, related_name='books', null=True, on_delete=models.SET_NULL)
    publisher = models.ForeignKey(Publisher, blank=True, null=True, on_delete=models.SET_NULL)
    is_read = models.BooleanField(default=False)
    book_pic = models.ImageField(upload_to='book', null=True, blank=True)
    summary = models.CharField(max_length=100, null=True, blank=True )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default="Roman")

    def __str__(self):
        return self.name