from django.db import models

# Create your models here.
class StockItem(models.Model): #stockitem_set.all()
	Name = models.ImageField(upload_to='image/', blank=True, null=True)
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True) # hello world -> hello-world
	partner_id = models.ForeignKey(User, default=1, on_delete=models.SET_NULL, null=True)
	content = models.TextField(null=True, blank=True)

	class Meta:
		ordering = ['-pk']

	def get_absolute_url(self):
	    return "/stock/{0}".format(self.slug)

	def get_edit_url(self):
	    return "{0}/edit".format(self.get_absolute_url())	    

	def get_delete_url(self):
	    return "{0}/delete".format(self.get_absolute_url())	   