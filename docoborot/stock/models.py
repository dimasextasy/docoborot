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
		return "{0}".format(self.slug)

	def get_edit_url(self):
		print(self.get_absolute_url())
		print("{0}/edit".format(self.get_absolute_url()))
		return "{0}/edit".format(self.get_absolute_url())	    

	def get_delete_url(self):
		return "/delete".format()


# Create your models here.
class Product(models.Model): #stockitem_set.all()
	name = models.CharField(max_length=120)
	title = models.CharField(max_length=120)
	purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
	selling_field = models.DecimalField(max_digits=10, decimal_places=2)
	stock_id = models.ForeignKey(StockItem, default=1, on_delete=models.CASCADE, null=False)

	class Meta:
		ordering = ['-pk']

	def get_absolute_url(self):
	    return "/product/{0}".format(self.slug)

	def get_edit_url(self):
	    return "{0}/edit".format(self.get_absolute_url())	    

	def get_delete_url(self):
	    return "{0}/delete".format(self.get_absolute_url())	   

class Partner(models.Model): #stockitem_set.all()
	name = models.CharField(max_length=120)
	surname = models.CharField(max_length=120)
	patronymic  = models.CharField(max_length=120)
	company_name   = models.CharField(max_length=120)

	class Meta:
		ordering = ['-pk']

	def get_absolute_url(self):
	    return "/partner/{0}".format(self.id)

	def get_create_url(self):
	    return "/partner-new/"    

	def get_edit_url(self):
	    return "{0}/edit".format(self.get_absolute_url())	    

	def get_delete_url(self):
	    return "{0}/delete".format(self.get_absolute_url())	   		   

class DealType(models.Model):
	value = models.CharField(max_length=120)

	class Meta:
		ordering = ['-pk']

class Deal(models.Model):
	partner_id = models.ForeignKey(Partner, default=1, on_delete=models.CASCADE, null=False)
	date = models.DateField()
	deal_type   = models.ForeignKey(DealType, default=1, on_delete=models.CASCADE, null=False)

	class Meta:
		ordering = ['-pk']

	def get_absolute_url(self):
	    return "/deal/{0}".format(self.id)

	def get_create_url(self):
	    return "/deal-new/"    

	def deal_get_edit_url(self):
	    return "{0}/edit".format(self.get_absolute_url())	    

	def get_delete_url(self):
	    return "{0}/delete".format(self.get_absolute_url())


class DealProduct(models.Model):
	deal_id = models.ForeignKey(Deal, default=1, on_delete=models.CASCADE, null=False)
	product_id = models.ForeignKey(Product, default=1, on_delete=models.CASCADE, null=False)
	count = models.DecimalField(max_digits=10, decimal_places=2)

	class Meta:
		ordering = ['-pk'] 

	    