from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class ArtPiece(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to="arts/")
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.name
