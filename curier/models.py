from django.db import models
from django.conf import settings
from django.utils import timezone
class Curier(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="mycurier")
	date_of_birth=models.DateField(blank=True, null=True)
	photo =models.ImageField(upload_to='curiers/%y/%m/%d', blank=True)
	experience=models.IntegerField(blank=True, null=True)
	phone = models.IntegerField(null=False, blank=False)
	is_available=models.BooleanField(default=False)
	balance = models.DecimalField(decimal_places=0,max_digits=1000,default=0)
class Changes(models.Model):
    user = models.ForeignKey(Curier,on_delete=models.CASCADE)
    balance_before= models.DecimalField(decimal_places=0,max_digits=1000,default=0)
    summa = models.DecimalField(decimal_places=0,max_digits=1000,default=0)
    reason = models.CharField(max_length=255)
    created_date=models.DateTimeField(default=timezone.now)