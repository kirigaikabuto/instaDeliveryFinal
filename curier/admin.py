from django.contrib import admin
from django import forms
from .models import Curier,Changes
from dal import autocomplete
class CurierAdmin(admin.ModelAdmin):
	model = Curier



class form(forms.ModelForm):
	class Meta:
		widgets = {
			'curier': autocomplete.ModelSelect2(url='curier-autocomplete')
		}

admin.site.register(Curier, CurierAdmin)
admin.site.register(Changes)
