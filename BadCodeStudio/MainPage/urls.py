from django.urls import path
from . import views

urlpatterns = [
    path('', views.objects_list.content_list, name='content_list'),
]