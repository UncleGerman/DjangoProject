from django.db import models
from django.utils.safestring import mark_safe


class Product(models.Model):
	title = models.CharField(max_length = 120)
	post = models.TextField()
	date = models.DateTimeField()
	image = models.ImageField(upload_to='media', null=True, blank=True)
	
	def  __str__(self):
		return self.title
