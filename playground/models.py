from django.db import models


class Product(models.Model):
    # title = models.CharField(max_length=255)
    # price = models.DecimalField(max_digits=5, decimal_places=3)
    # inventory = models.IntegerField()
    # last_update = models.DateTimeField(auto_now=True)
    pass


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
