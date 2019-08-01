from django.shortcuts import render
from django.views.generic import ListView
from reports.models import Rapport

#### class and function to handle the search request and filter by request ####

class SearchRapportListView(ListView):
	template_name = "search.html"

	def get_queryset(self, *args, **kwargs):
		request = self.request
		query = request.GET.get('q')
		if query is not None:
			queryset = Rapport.objects.all()
			print(query)
			print(Rapport.objects.filter(namn__startswith=query).values())
			print(Rapport.objects.all().count())
			if Rapport.objects.filter(reportNr__iexact=query):
				return Rapport.objects.filter(reportNr__iexact=query).order_by('-date')
			if Rapport.objects.filter(avd__iexact=query):
				return Rapport.objects.filter(avd__iexact=query)
			if Rapport.objects.filter(ritningNr__iexact=query):
				return Rapport.objects.filter(ritningNr__iexact=query).order_by('-date')
			if Rapport.objects.filter(enhetsNr__iexact=query):
				return Rapport.objects.filter(enhetsNr__iexact=query).order_by('-date')
			if Rapport.objects.filter(atgard__iexact=query):
				return Rapport.objects.filter(atgard__iexact=query).order_by('-date')
			if Rapport.objects.filter(namn__iexact=query):
				return Rapport.objects.filter(namn__iexact=query).order_by('-date')
			if Rapport.objects.filter(anstNr__iexact=query):
				return Rapport.objects.filter(anstNr__iexact=query).order_by('-date')


		return Rapport.objects.none()


# Create your views here.
