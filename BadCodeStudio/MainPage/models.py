from django.db import models

class Content(models.Model):
	article_text = models.TextField()
	article_img = models.ImageField(
		upload_to='media', null=True, blank=True)

class Slider(models.Model):
	slider_img = models.ImageField(
		upload_to='media', null=True, blank=True)
	slider_text = models.TextField()
	slider_title = models.CharField(max_length = 120)