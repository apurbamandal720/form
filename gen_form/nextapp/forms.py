from django import forms  
from .models import *

class re_meForm(forms.ModelForm):
	class Meta:
		model= re_me
		fields="__all__"