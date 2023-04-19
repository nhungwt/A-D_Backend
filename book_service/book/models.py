from django.db import models
from django.urls import reverse

GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]

class Author(models.Model):
    full_name = models.CharField(max_length=100, null=True, default="")
    pseudonym = models.CharField(max_length=100)  # nghệ danh
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return self.full_name


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        db_table = 'publisher'

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True, default="", help_text='')
    image = models.CharField(max_length=500, null=True)
    description = models.CharField(max_length=100)
    # Tổng là 9 số, trong đó có 2 số thập phân
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(
        Publisher, unique=False, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'book'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("name", kwargs={"slug": self.slug})
