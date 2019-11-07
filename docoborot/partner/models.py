from django.db import models

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