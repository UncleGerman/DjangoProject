from django.shortcuts import render
from .models import Content

class objects_list(object):
	"""docstring for ClassName"""
	def content_list(request, artical_list = Content.objects.all()):
		return render(request, 'MainPage/Content.html', {"artical_list" : artical_list})
		