from django.conf import settings
from django.db import models
from django.db.models import Q

# Create your models here.
User = settings.AUTH_USER_MODEL

class StockItemQuerySet(models.QuerySet):
	def search(self, query):
		lookup = (Q(title__icontains=query) |
			      Q(content__icontains=query))
		return self.filter(lookup)

class StockItemManager(models.Manager):
	def get_queryset(self):
		return StockItemQuerySet(self.model, using=self._db)

	def search(self, query=None):
		if query is None:
			return self.get_queryset().none()
		return self.get_queryset().search(query)


class StockItem(models.Model): #stockitem_set.all()
	contractor = models.ForeignKey(User, default=1, on_delete=models.SET_NULL, null=True)
	image = models.ImageField(upload_to='image/', blank=True, null=True)
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True) # hello world -> hello-world
	content = models.TextField(null=True, blank=True)

	class Meta:
		ordering = ['-pk']

	def get_absolute_url(self):
	    return "/stock/{0}".format(self.slug)

	def get_edit_url(self):
	    return "{0}/edit".format(self.get_absolute_url())	    

	def get_delete_url(self):
	    return "{0}/delete".format(self.get_absolute_url())	   
