from django.db import models

from django.conf import settings
import decimal
from django.utils import timezone
from curier.models import Curier
class Lalo(models.Model):
	author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	title=models.CharField(max_length=200)
	otkuda=models.TextField(max_length=200)
	kontakt1=models.TextField()
	kuda=models.TextField()
	kontakt2=models.TextField()
	Ves=models.DecimalField(decimal_places=0,max_digits=1000,default=10)
	Price=models.DecimalField(decimal_places=0,max_digits=1000,default=10)

	created_date=models.DateTimeField(default=timezone.now)
	published_date=models.DateTimeField(blank=True,null=True)
	class Meta:
		ordering=("-created_date",)
	def __str__(self):
		return self.title

	def publishe(self):
		self.published_date=timezone.now()
		self.save()
class TestOrder(models.Model):
	client=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	marshrut=models.CharField(max_length=200)
	ves=models.DecimalField(decimal_places=0,max_digits=1000,default=10)
	from_address=models.CharField(max_length=200)
	from_phone=models.CharField(max_length=200)
	from_comment=models.CharField(max_length=200)
	to=models.CharField(max_length=200)
	to_phone=models.CharField(max_length=200)
	to_date=models.CharField(max_length=200)
	to_date_until=models.CharField(max_length=200)	
	to_comment=models.CharField(max_length=200)
	distance=models.DecimalField(decimal_places=0,max_digits=1000,default=10)
	itog=models.DecimalField(decimal_places=0,max_digits=1000,default=10)
	curier = models.ForeignKey(Curier,on_delete=models.CASCADE,default=None,related_name="choiced_curier",blank=True,null=True)
	nal=models.DecimalField(decimal_places=0,max_digits=1000,default=0)
	raschet=models.DecimalField(decimal_places=0,max_digits=1000,default=0)
	status = models.CharField(max_length=200,default="Ожидание")
	curier_money = models.DecimalField(decimal_places=0,max_digits=1000,default=0)
	__original_curier = None 

	def __init__(self,*args,**kwargs):
		print("Object was created")
		super(TestOrder,self).__init__(*args,**kwargs)
		self.__origin_curier = self.curier

	def save(self,force_insert=False,force_update=False,*args,**kwargs):
		if self.curier is None:
			self.__origin_curier = self.curier
			# self.curier_money = (self.itog*65)//100
			super(TestOrder,self).save(force_insert,force_update,*args,**kwargs)
		elif self.curier != self.__origin_curier:
			# self.curier.balance-=(self.itog*35)//100
			if self.curier.balance>=0:
				self.curier.save()
				super(TestOrder,self).save(force_insert,force_update,*args,**kwargs)
				self.__origin_curier = self.curier
		else:
			super(TestOrder,self).save(force_insert,force_update,*args,**kwargs)




