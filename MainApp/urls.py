from django.conf.urls import url, include
from . import views
from MainApp.views import ContentList

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Content/$', ContentList.as_view()),
]
