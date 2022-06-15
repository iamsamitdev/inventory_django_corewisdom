from django.db import models

# Create your models here.
# ชื่อตารางจะมาจาก แอพ_คลาส
# stock_product
class Product(models.Model):
    product_name = models.CharField(max_length=128)
    product_detail = models.TextField()
    product_barcode = models.CharField(max_length=13)
    product_qty = models.IntegerField()
    product_price = models.DecimalField(decimal_places=2, max_digits=7)
    product_image = models.CharField(max_length=128)
    product_status = models.IntegerField()