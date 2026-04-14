from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ("laptops", "Laptops"),
        ("phones", "Phones"),
        ("accessories", "Accessories"),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(blank=True)

    stock = models.IntegerField(default=0)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="laptops"
    )

    def __str__(self):
        return self.name