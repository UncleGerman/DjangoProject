from django.conf.urls import url, include
from django.urls import path
from . import views

from .views import AboutPageView, ContactPageView, SearchResultsView

urlpatterns = [

    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    
    #Cart
    path('cart/', views.cart_detail, name='cart_detail'),

    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),

    #Products
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),

    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),

    url(r'^create/$', views.order_create, name='order_create'),
]