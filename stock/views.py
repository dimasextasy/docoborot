from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

# Create your views here.
from .forms import StockItemModelForm
from .models import StockItem


def stock_item_list_view(request):
	qs = StockItem.objects.all()
	template_name = 'stock_item/list.html'
	context = {'object_list': qs}
	return render(request, template_name, context)


#@login_required
@staff_member_required
def stock_item_create_view(request):
	form = StockItemModelForm(request.POST or None)
	if form.is_valid():
	    #obj = StockItem.objects.create(**form.cleaned_data)
	    obj = form.save(commit=False)
	    obj.contractor = request.user
	    obj.save()
	    form = StockItemModelForm()
	template_name = 'form.html'
	context = {
	    "form": form
	}
	return render(request, template_name, context)

def stock_item_detail_view(request, slug):
	obj = get_object_or_404(StockItem, slug=slug)
	template_name = 'stock_item/detail.html'
	context = {"object": obj}
	return render(request, template_name, context)

@staff_member_required
def stock_item_update_view(request, slug):
	obj = get_object_or_404(StockItem, slug=slug)
	my_form = StockItemModelForm(request.POST or None, instance=obj)
	if my_form.is_valid():
		my_form.save()
	template_name = 'form.html'
	context = {"form": my_form, "title": "Update{}".format(obj.title) }
	return render(request, template_name, context)

@staff_member_required
def stock_item_delete_view(request, slug):
	obj = get_object_or_404(StockItem, slug=slug)
	template_name = 'stock_item/delete.html'
	if request.method == "POST":
		obj.delete()
		return redirect("/stock")
	context = {"object": obj}
	return render(request, template_name, context)	      	        