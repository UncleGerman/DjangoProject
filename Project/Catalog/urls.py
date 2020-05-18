from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from Catalog.models import Product
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$',
    ListView.as_view(queryset=Product.objects.all().order_by("-date")[:20],
    template_name="Catalog/Products.html")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
