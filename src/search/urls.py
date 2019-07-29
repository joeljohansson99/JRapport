from django.conf.urls import url

from .views import SearchRapportListView

urlpatterns = [
	url(r'^$', SearchRapportListView.as_view(), name="query")
]