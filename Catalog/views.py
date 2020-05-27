from django.shortcuts import render

def index(request):
	return render(request, 'MainApp/main_templates.html')
