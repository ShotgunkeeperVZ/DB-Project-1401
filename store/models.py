from django.db import models


class Product(models.Model):
    pass


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
