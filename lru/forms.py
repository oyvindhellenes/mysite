from django import forms
from django.forms import ModelChoiceField, DateTimeField
from django.contrib.admin import widgets

from models import Utstyr, Reservasjon

class UtstyrForm(forms.ModelForm):
	
	class Meta:
		model = Utstyr
		
class ReservationForm(forms.ModelForm):
	
	class Meta:
		model = Reservasjon
		widgets = {'reservert_av': forms.HiddenInput(),'utstyr': forms.HiddenInput()}
		

		
class UtstyrsListeForm(forms.ModelForm):
	
	class Meta:
		model = Utstyr
		exclude = ['beskrivelse', 'utstyrstype','lokasjon']		
	
	utstyr = forms.ModelChoiceField(queryset=Utstyr.objects.all())


		
		