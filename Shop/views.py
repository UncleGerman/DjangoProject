#import
from django.contrib.auth.models import User
from django.shortcuts import render, redirect , get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import ListView, TemplateView
from django.db.models import Q

#models
from .models import Category, Product, OrderItem, Order

#.py
from .cart import Cart
from .forms import CartAddProductForm, OrderCreateForm

class AboutPageView(TemplateView):
    template_name = 'Shop/about.html'
    
class ContactPageView(TemplateView):
    template_name = 'Shop/contact.html'


def product_list(request, category_slug = None):

	category = None

	categories = Category.objects.all()

	products = Product.objects.filter(available = True)

	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)

	cart_product_form = CartAddProductForm()

	data = {'category': category,'categories': categories,'products': products, 
    'cart_product_form': cart_product_form}

	return render(request, 'Shop/Shops.html', context = data)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id = id, slug = slug, available = True)

    categories = Category.objects.all()

    cart_product_form = CartAddProductForm()

    data = {'product': product, 'cart_product_form': cart_product_form,'categories': categories}

    return render(request, 'Shop/Product.html', context = data) 

#Cart
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id = product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product = product, quantity = cd['quantity'], update_quantity = cd['update'])
    return redirect('shop:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id = product_id)
    cart.remove(product)
    return redirect('shop:cart_detail')


def cart_detail(request):

    cart = Cart(request)

    categories = Category.objects.all()

    data = {'cart': cart, 'categories' : categories}

    return render(request, 'Cart/cart.html', data)


class SearchResultsView(ListView):
    model = Product
    template_name = 'Search/search_results.html'

    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(product_name__icontains=query)
        )
        return object_list

def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'Cart/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'Cart/create.html',
                  {'cart': cart, 'form': form})
def discount(request):
    if valid_to >= timezone.now():
        active = False
        discounts = models.Product(active = active)
        discounts.save()