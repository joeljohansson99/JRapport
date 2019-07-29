from django.db import models
from datetime import datetime
import os

class RapportQuerySet(models.query.QuerySet):

	def active(self):
		return self.filter()

class RapportManager(models.Manager):

	def get_queryset(self):
		return RapportQuerySet(self.model, using=self._db)
	
	def all(self):
		return self.get_queryset().active()


class Rapport(models.Model):

	objects = RapportManager()

	reportNr    = models.TextField(blank=True)
	avd	        = models.TextField(max_length=10, null=True, blank=True)
	ritningNr 	= models.TextField(max_length=20, null=True, blank=True)
	enhetsNr 	= models.TextField(max_length=40, null=True, blank=True)
	atgard	    = models.TextField(max_length=100,null=True, blank=True)
	namn	    = models.TextField(max_length=100,null=True, blank=True)
	anstNr	    = models.TextField(max_length=100,null=True, blank=True)
	date		= models.DateTimeField(auto_now_add=True)
	file 		= models.FileField(upload_to='files', null=True, blank=True)

	def __str__(self):
		return self.reportNr