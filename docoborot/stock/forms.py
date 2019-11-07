from django import forms

from .models import StockItem
from .models import Partner

class StockItemForm(forms.Form):
	title = forms.CharField()
	slug = forms.SlugField()
	content = forms.CharField(widget=forms.Textarea)


class StockItemModelForm(forms.ModelForm):
	class Meta:
		model = StockItem
		fields = ['title', 'image', 'slug', 'content']


	def clean_title(self, *args, **kwargs):
		instance = self.instance
		title = self.cleaned_data.get('title')
		qs = StockItem.objects.filter(title__iexact=title)
		if instance is not None:
			qs = qs.exclude(pk=instance.pk)
		if qs.exists():
		    raise forms.ValidationError("This title has already been used. Please try again.")
		return title		




class PartnerForm(forms.Form):
	name = forms.CharField()
	surname = forms.CharField()
	patronymic = forms.CharField()
	company_name = forms.CharField()


class PartnerModelForm(forms.ModelForm):
	class Meta:
		model = Partner
		fields = ['name', 'surname', 'patronymic', 'company_name']		