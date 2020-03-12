from django import forms
from .models import Lalo

class PostForm(forms.ModelForm):
	class Meta:
		model=Lalo
		fields=('title','otkuda','kontakt1','kuda','kontakt2','Ves','Price')
		