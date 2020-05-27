from django.db import models

class Content(models.Model):
	article_text = models.TextField()
	article_img = models.ImageField(upload_to='media', null=True, blank=True)

	def __str__(self):
		return self.article_text