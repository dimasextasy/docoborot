from django import forms

from .models import Partner

class PartnerForm(forms.Form):
	name = forms.CharField()
	surname = forms.CharField()
	patronymic = forms.CharField()
	company_name = forms.CharField()


class PartnerModelForm(forms.ModelForm):
	class Meta:
		model = Partner
		fields = ['name', 'surname', 'patronymic', 'company_name']