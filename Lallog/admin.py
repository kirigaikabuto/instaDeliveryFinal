from django.contrib import admin

from .models import Lalo,TestOrder
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field


class TestOrderResource(resources.ModelResource):
	client_name=Field()
	curier_name=Field()
	class Meta:
		model = TestOrder
	def dehydrate_client_name(self,order):
		return "%s"%order.client.username
	def dehydrate_curier_name(self,order):
		if order.curier is not None:
			return order.curier.user.username
		else:
			return "Курьера нет"
class TestOrderAdmin(ImportExportModelAdmin):
	resource_class=TestOrderResource


admin.site.register(TestOrder,TestOrderAdmin)