from django.db import models

class ProductCategory(models.Model):
	name = models.CharField(max_length = 60, blank = True, null = True, default = None)

class Product(models.Model):
	name = models.CharField(max_length = 60, blank = True, null = True, default = None)
	description = models.TextField(blank = True, null = True, default = None)
	img_product = models.ImageField()
	category = models.ForeignKey(ProductCategory, blank = True, null = True, default = None, on_delete=models.CASCADE)
		