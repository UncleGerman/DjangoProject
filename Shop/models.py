from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings


class Category(models.Model):
	category_name = models.CharField(
		max_length = 60, blank = True, null = True, default = None)
	slug = models.SlugField(
		max_length = 200, db_index = True, unique = True)
	category_img = models.ImageField(
		upload_to = 'media', null = True, blank = True)

	class Meta:
		ordering = ["category_name"]

		#
		verbose_name = "Категория"
		verbose_name_plural = "Категории"
			
	def  __str__(self):
		return self.category_name

	def get_absolute_url(self):
		return reverse('shop:product_list_by_category', args = [self.slug])
		
class Product(models.Model):

	category = models.ForeignKey(Category, on_delete = models.CASCADE)

	slug = models.SlugField(
		max_length = 200, db_index = True, default = None)
	
	product_name  = models.CharField(
		max_length = 60, blank = True, null = True, default = None)

	product_description  = models.TextField()

	product_img = models.ImageField(
		upload_to = 'media', null = True, blank = True)

	product_price = models.FloatField(default = 0.0)

	available = models.BooleanField(default = True)

	product_stock = models.PositiveIntegerField(default = 0)

	active = models.BooleanField(default = True)
	
	class Meta:
		ordering = ["product_name"]
		verbose_name = "Продукт"
		verbose_name_plural = "Продукты"
		index_together = ["id", "slug"]

	def  __str__(self):
		return self.product_name
		
	def get_absolute_url(self):
		return reverse('shop:product_detail', args = [self.id, self.slug])

class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
