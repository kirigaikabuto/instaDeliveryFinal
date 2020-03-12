from django.db import models
from Lallog.models import Lalo
from curier.models import Curier
# Create your models here.
class Order(models.Model):
	lid = models.ForeignKey(Lalo,related_name="myorders",on_delete=models.CASCADE)
	curier = models.ForeignKey(Curier,related_name="client_orders",on_delete=models.CASCADE,blank=True,null=True)