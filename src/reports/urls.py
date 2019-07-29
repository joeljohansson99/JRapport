from django.conf.urls import url

from .views import RapportListView

urlpatterns = [
	url(r'^$', RapportListView.as_view(), name="query")
]