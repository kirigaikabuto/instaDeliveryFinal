from django.db import models
from django.conf import settings
# Create your models here.


class AdminModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="myadmin")
    phone = models.IntegerField(null=False, blank=False)



    def __str__(self):
        return self.user.username