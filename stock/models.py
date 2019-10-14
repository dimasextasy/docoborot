from django.conf import settings
from django.db import models

# Create your models here.
User = settings.AUTH_USER_MODEL

class StockItem(models.Model): #stockitem_set.all()
	contractor = models.ForeignKey(User, default=1, on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True) # hello world -> hello-world
	content = models.TextField(null=True, blank=True)


	def get_absolute_url(self):
	    return "/stock/{0}".format(self.slug)

	def get_edit_url(self):
	    return "{0}/edit".format(self.get_absolute_url())	    

	def get_delete_url(self):
	    return "{0}/delete".format(self.get_absolute_url())	   
