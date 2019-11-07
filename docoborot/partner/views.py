from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

# Create your views here.
from .forms import PartnerModelForm
from .models import Partner


def partner_list_view(request):
	qs = Partner.objects.all()
	template_name = 'partner/list.html'
	context = {'object_list': qs}
	return render(request, template_name, context)


#@login_required
@staff_member_required
def partner_create_view(request):
	form = PartnerModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
	    #obj = Partner.objects.create(**form.cleaned_data)
	    obj = form.save(commit=False)
	    obj.contractor = request.user
	    obj.save()
	    form = PartnerModelForm()
	template_name = 'form.html'
	context = {
	    "form": form
	}
	return render(request, template_name, context)

def partner_detail_view(request, id):
	obj = get_object_or_404(Partner, id=id)
	template_name = 'partner/detail.html'
	context = {"object": obj}
	return render(request, template_name, context)

@staff_member_required
def partner_update_view(request, id):
	obj = get_object_or_404(Partner, id=id)
	my_form = PartnerModelForm(request.POST or None, instance=obj)
	if my_form.is_valid():
		my_form.save()
	template_name = 'form.html'
	context = {"form": my_form, "title": "Update {}".format(obj.company_name) }
	return render(request, template_name, context)

@staff_member_required
def partner_delete_view(request, id):
	obj = get_object_or_404(Partner, id=id)
	template_name = 'partner/delete.html'
	if request.method == "POST":
		obj.delete()
		return redirect("/partner")
	context = {"object": obj}
	return render(request, template_name, context)	 