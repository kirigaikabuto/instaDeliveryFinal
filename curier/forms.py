from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Curier

class CurierRegisterForm(forms.ModelForm):

	class Meta:
		model = Curier
		fields=('first_name','last_name','photo','experience','phone')
