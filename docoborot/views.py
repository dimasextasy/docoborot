from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
	my_title = "hello universe!"
	return render(request, "home.html", {"title": my_title, "my_list": [1, 2, 3, 4, 5]})

def about_page(request):
	my_title = "hello universe!"
	return render(request, "about.html", {"title": "ABOUT USS"})	

def example_page(request):
	context = {"title":"Example"}
	template_name = "hello_world.html"
	template_obj = get_template(template_name)
	rendered_obj = template_obj.render(context)
	return HttpResponse()
 