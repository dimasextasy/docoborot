from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import BlogPostModelForm, PartnerModelForm
from .models import BlogPost, Partner, Stock, Product

# CRUD

# GET -> Retrieve / List

# POST -> Create / Update / DELETE

# Create Retrieve Update Delete

def get_object_by_url_name(object_name):
    object_list = {
    'blog': BlogPost,
    'partner': Partner,
    'stock': Stock,
    'product': Product
    }
    return object_list[object_name]

def get_object_form_by_url_name(request, object_name):
    object_form_list = {
    'blog': BlogPostModelForm(request.POST or None, request.FILES or None),
    'partner': PartnerModelForm(request.POST or None, request.FILES or None),
    'stock': Stock,
    'product': Product
    }
    return object_form_list[object_name]


def get_object_form_by_url_name_with_instance(request, object_name, obj):
    object_form_list = {
    'blog': BlogPostModelForm(request.POST or None, instance=obj),
    'partner': PartnerModelForm(request.POST or None, instance=obj),
    'stock': Stock,
    'product': Product
    }
    return object_form_list[object_name]


def objects_list_view(request, object_name):
    # list out objects 
    # could be search
    current_object = get_object_by_url_name(object_name)
    qs = current_object.objects.all() 
    template_name = 'blog/list.html'
    context = {'object_list': qs}
    return render(request, template_name, context) 


def blog_post_list_view(request):
    # list out objects 
    # could be search
    qs = BlogPost.objects.all().published() # queryset -> list of python object
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    template_name = 'blog/list.html'
    context = {'object_list': qs}
    return render(request, template_name, context) 

# @login_required
@staff_member_required
def objects_create_view(request, object_name):
    # create objects
    # ? use a form
    # request.user -> return something
    print(object_name)
    form = get_object_form_by_url_name(request, object_name)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return redirect("/blog/{0}".format(object_name))
    template_name = 'form.html'
    context = {'form': form}
    return render(request, template_name, context)


# @login_required
@staff_member_required
def blog_post_create_view(request):
    # create objects
    # ? use a form
    # request.user -> return something
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()
    template_name = 'form.html'
    context = {'form': form}
    return render(request, template_name, context)  


def objects_detail_view(request, object_name, slug):
    # 1 object -> detail view
    obj = get_object_or_404(get_object_by_url_name(object_name), slug=slug)
    template_name = 'blog/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    # 1 object -> detail view
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)   


@staff_member_required
def objects_update_view(request, object_name, slug):
    obj = get_object_or_404(get_object_by_url_name(object_name), slug=slug)
    form = get_object_form_by_url_name_with_instance(request, object_name, obj)
    if form.is_valid():
        form.save()
    template_name = 'form.html'
    context = {"title": "Update {0}".format(obj.title), "form": form}
    return render(request, template_name, context)


@staff_member_required
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'form.html'
    context = {"title": "Update {0}".format(obj.title), "form": form}
    return render(request, template_name, context)  

@staff_member_required
def objects_delete_view(request, object_name, slug):
    obj = get_object_or_404(get_object_by_url_name(object_name), slug=slug)
    template_name = 'blog/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/blog")
    context = {"object": obj}
    return render(request, template_name, context)  


@staff_member_required
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/blog")
    context = {"object": obj}
    return render(request, template_name, context)  









