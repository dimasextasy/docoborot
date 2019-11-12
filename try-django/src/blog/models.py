from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils import timezone
# Create your models here.

User = settings.AUTH_USER_MODEL


class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)

    def search(self, query):
        lookup = (
                    Q(title__icontains=query) |
                    Q(content__icontains=query) |
                    Q(slug__icontains=query) |
                    Q(user__first_name__icontains=query) |
                    Q(user__last_name__icontains=query) |
                    Q(user__username__icontains=query)
                    )

        return self.filter(lookup)


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)


class BlogPost(models.Model): # blogpost_set -> queryset
    # id = models.IntegerField() # pk
    user    = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    image   = models.ImageField(upload_to='image/', blank=True, null=True)
    title  = models.CharField(max_length=120)
    slug   = models.SlugField(unique=True) # hello world -> hello-world
    content  = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = BlogPostManager()

    class Meta:
        ordering = ['-publish_date', '-updated', '-timestamp']

    def get_absolute_url(self):
        return "/blog/{0}".format(self.slug)

    def get_edit_url(self):
        return "{0}/edit".format(self.get_absolute_url())

    def get_delete_url(self):
        return "{0}/delete".format(self.get_absolute_url())


class StockItem(models.Model):
    name  = models.CharField(max_length=120)


class Product(models.Model): #stockitem_set.all()
    name = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_field = models.DecimalField(max_digits=10, decimal_places=2)
    stock_id = models.ForeignKey(StockItem, default=1, on_delete=models.CASCADE, null=False)


class Partner(models.Model): #stockitem_set.all()
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    patronymic  = models.CharField(max_length=120)
    company_name   = models.CharField(max_length=120)


class DealType(models.Model):
    value = models.CharField(max_length=120)


class Deal(models.Model):
    partner_id = models.ForeignKey(Partner, default=1, on_delete=models.CASCADE, null=False)
    date = models.DateField()
    deal_type   = models.ForeignKey(DealType, default=1, on_delete=models.CASCADE, null=False)


class DealProduct(models.Model):
    deal_id = models.ForeignKey(Deal, default=1, on_delete=models.CASCADE, null=False)
    product_id = models.ForeignKey(Product, default=1, on_delete=models.CASCADE, null=False)
    count = models.DecimalField(max_digits=10, decimal_places=2)