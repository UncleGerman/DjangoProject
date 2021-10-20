from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm, ProductForm, CategoryForm, ProductUpdateForm, CategoryUpdateForm, OrderUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from Shop.models import Order, OrderItem, Product, Category
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})
@login_required
def orderviews(request):
    data = {'orderitem' : OrderItem.objects.all()[:5]}
    return render(request, 'account/order.html', context = data)
@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,
                      'account/edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})
@login_required
def dashboard(request):
    data = {'section' : 'dashboard'}
    return render(request, 'dashboard.html', context = data)

#Products function Admin
@login_required
def all_product(request):
    data = {'product' : Product.objects.all()}
    return render(request, 'account/admin/product.html', context = data)

@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
    else:
        form = ProductForm()
    return render(request, 'account/admin/add_product.html', {'form': form})

    def get_success_url(self):
        return reverse('account:all_product')

class UpdateProductView(UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = 'account/admin/update_product.html'

    def get_success_url(self):
        return reverse('account:all_product')

class DeleteProductView(DeleteView):
    model = Product
    template_name = 'account/delete.html'

    def get_success_url(self):
        return reverse('account:all_product')
               
#Category function Admin 
@login_required
def all_category(request):
    data = {'category' : Category.objects.all()}
    return render(request, 'account/admin/category.html', context = data)

@login_required
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
    else:
        form = CategoryForm()
    return render(request, 'account/admin/add_category.html', {'form': form})

    def get_success_url(self):
        return reverse('account:all_category')

class UpdateCategoryView(UpdateView):
    model = Category
    form_class = CategoryUpdateForm
    template_name = 'account/admin/update_category.html'

    def get_success_url(self):
        return reverse('account:all_category')

#Order fubction Admin
@login_required
def all_order(request):
    data = {'orders' : OrderItem.objects.all()}
    return render(request, 'account/admin/order_admin.html', context = data)
    
class UpdateOrderView(UpdateView):
    model = Order
    form_class = OrderUpdateForm
    template_name = 'account/admin/update_order.html'

    def get_success_url(self):
        return reverse('account:all_order_admin')

class DeleteOrderView(DeleteView):
    model = Order
    template_name = 'account/delete.html'

    def get_success_url(self):
        return reverse('account:all_order_admin')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})