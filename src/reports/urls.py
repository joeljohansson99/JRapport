from django.conf.urls import url

from .views import RapportListView

#### url pattern for main page ####

urlpatterns = [
	url(r'^$', RapportListView.as_view(), name="query")
]