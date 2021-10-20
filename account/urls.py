from django.urls import path
from django.conf.urls import url

from . import views

from .views import UpdateProductView, UpdateCategoryView, UpdateOrderView, DeleteOrderView, DeleteProductView

from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name = 'account'

urlpatterns = [
    path("login/", LoginView.as_view(template_name='registration/login.html'), name="user_login"),

    path("logout/", LogoutView.as_view(template_name = 'registration/logged_out.html'), name="user_logout"),

    path('logout-then-login/', auth_views.logout_then_login, name='logout_then_login'),

    path('password-change/', PasswordChangeView.as_view(template_name='account/password_change_form.html'), name='password_change'),
	path('password-change/done/', PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'), name='password_change_done'),

	path('password-reset/', PasswordResetView.as_view(template_name='account/password_reset_form.html'), name='password_reset'),
	path('password-reset/done/', PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
	path('password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/', PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'), name='password_reset_confirm'),
	path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name='password_reset_complete'),

    path("dashboard/", views.dashboard, name='dashboard'),

    #ProductsAdmin
    path('admin/product', views.all_product, name = "all_product"),
    path('admin/product/addproduct', views.add_product, name = "add_product"),
    path('<pk>/delete/', DeleteProductView.as_view(), name = "delete_product"),
    url(r'^updateproduct/(?P<pk>\d+)/$',UpdateProductView.as_view(), name='update_product'),


    #OrdersAdmin
    path('admin/order', views.all_order, name = 'all_order_admin'),
    path('<pk>/delete/', DeleteOrderView.as_view(), name = "delete_order"),
    url(r'^updateorder/(?P<pk>\d+)/$',UpdateOrderView.as_view(), name='update_order'),

    #CategoryAdmin
    path('admin/category', views.all_category, name = 'all_category'),
    path('admin/product/addcategory', views.add_category, name = "add_category"),
    url(r'^updatecategor/(?P<pk>\d+)/$',UpdateCategoryView.as_view(), name='update_category'),

    path("order/", views.orderviews, name='all_order'),

    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]