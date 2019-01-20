from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	return HttpResponse("<h1>Hello World</h1>")

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
	my_content = {
		"my_text" : "this is the view",
		"my_number": 123,
		"my_list": [13, 42, 53]
	}
	return render(request, "about.html", {})