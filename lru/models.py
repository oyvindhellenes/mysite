from django.db import models
from django.utils import timezone
import datetime

class Utstyr(models.Model):
	utstyrstype = models.CharField(max_length=100)
	beskrivelse = models.CharField(max_length=300)
	lokasjon = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.utstyrstype
	
class Reservasjon(models.Model):
	utstyr = models.ForeignKey(Utstyr)
	dato = models.DateTimeField('Reservasjons dato')
	reservert_av = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.utstyr.utstyrstype +" reservert av "+ self.reservert_av + " den " + self.dato.strftime("%Y-%m-%d %H:%M:%S")
		
 
