from django import forms

from .models import StockItem

class StockItemForm(forms.Form):
	title = forms.CharField()
	slug = forms.SlugField()
	content = forms.CharField(widget=forms.Textarea)


class StockItemModelForm(forms.ModelForm):
	class Meta:
		model = StockItem
		fields = ['title', 'slug', 'content']


	def clean_title(self, *args, **kwargs):
		instance = self.instance
		title = self.cleaned_data.get('title')
		qs = StockItem.objects.filter(title__iexact=title)
		if instance is not None:
			qs = qs.exclude(pk=instance.pk)
		if qs.exists():
		    raise forms.ValidationError("This title has already been used. Please try again.")
		return title		