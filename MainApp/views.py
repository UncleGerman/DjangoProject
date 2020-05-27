from django.shortcuts import render
from django.views.generic import ListView
from MainApp.models import Content

class ContentList(ListView):
    model = Content


def index(request):
	return render(request, 'Content.html')


def generate_path(instance, filename):
    ext = filename.rsplit('.', 1)[-1]
    h = md5(instance.user.username.encode()).hexdigest()
    result = 'photos/%s/%s/%s.%s' % (h[:2], h[2:4], h[4:], ext)
    path = os.path.join(settings.MEDIA_ROOT, result)
    if os.path.exists(path):
        os.remove(path)
    return result