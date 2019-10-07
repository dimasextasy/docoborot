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