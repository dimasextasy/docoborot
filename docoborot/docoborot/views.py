from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm
from stock.models import StockItem

def home_page(request):
	my_title = "Лабораторный проект по Документообороту"
	qs = StockItem.objects.all()[:5]
	context = {"title": my_title, "stock_list": qs}
	return render(request, "home.html", context)

def about_page(request):
	my_title = "hello universe!"
	return render(request, "about.html", {"title": "ABOUT USS"})

def contact_page(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form = ContactForm()
	context = {
		"title": "Contact USS",
		"form": form
	}
	return render(request, "form.html",context)

def example_page(request):
	context = {"title":"Example"}
	template_name = "hello_world.html"
	template_obj = get_template(template_name)
	rendered_obj = template_obj.render(context)
	return HttpResponse()
 