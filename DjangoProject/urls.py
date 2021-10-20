from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include

from django.conf import settings
from django.views.static import serve

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	
	path('admin/', admin.site.urls),

	path('', include(('Shop.urls', 'shop'), namespace='shop')), 

	url(r'^account/', include('account.urls')),

    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

