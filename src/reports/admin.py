from django.contrib import admin

from django.forms import TextInput, Textarea
from django.db import models

from .models import Rapport

#### Displays the model reports for the admin site ####

class RapportAdmin(admin.ModelAdmin):
	list_display=['__str__']

	formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':1})},
    }

	class Meta:
		model = Rapport



admin.site.register(Rapport, RapportAdmin)

# Register your models here.
