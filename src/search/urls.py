from django.conf.urls import url

from .views import SearchRapportListView

#### url pattern for the search page ####

urlpatterns = [
	url(r'^$', SearchRapportListView.as_view(), name="query")
]