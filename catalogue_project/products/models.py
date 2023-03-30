from django.db import models

# Create your models here.


class Products(models.Model):
    item_code = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255)
    category_l1 = models.CharField(max_length=255)
    category_l2 = models.CharField(max_length=255)
    upc = models.CharField(max_length=255)
    parent_code = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(default=False)

    class Meta:
        db_table = 'products_table'
