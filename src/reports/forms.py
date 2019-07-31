from django import forms
from reports.models import Rapport
from django.forms import DateTimeInput

class AddReportTypeForm(forms.Form):
	avd = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control bars', 'placeholder':'R8'}))
	ritningNr = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control bars', 'placeholder':'3-1711'}))
	enhetsNr = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control bars', 'placeholder':'B394'}))
	atgard = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows':4, 'cols':30, 'class':'form-control bars', 'placeholder':'Ökade hastigheten på bandet 5% p.g.a större flöde'}))
	namn = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control bars', 'placeholder':'Erik Johansson'}))
	anstNr = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control bars', 'placeholder':'43011'}))
	date = forms.DateTimeField(required=True, widget=forms.DateTimeInput(attrs={'class': 'datetime-input form-control bars'}))
	file = forms.FileField(required=False, widget=forms.FileInput())

	class Meta:
		model = Rapport
	
	def __init__(self, *args, **kwargs):
		super(AddReportTypeForm, self).__init__(*args, **kwargs)
		self.fields['avd'].label = "Avdelning"
		self.fields['ritningNr'].label = "Ritnings Nummer"
		self.fields['enhetsNr'].label = "Enhets Nummer"
		self.fields['atgard'].label = "Åtgärd"
		self.fields['namn'].label = "Namn"
		self.fields['anstNr'].label = "Anställnings Nummer"
		self.fields['date'].label = "Datum och Tid"
		self.fields['file'].label = "Bilaga"
		