from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.views.static import serve

urlpatterns = [
	url(r'^', include ('MainApp.urls')),
	url(r'^Catalog/', include('Catalog.urls')),
	#
    url('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
