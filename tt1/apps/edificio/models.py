from django.db import models

# Create your models here.

CHOICES = (
	('0',0),
	('1',1),
	('2',2)
	)

class Edificio(models.Model):

	nombre = models.CharField(max_length=50)
	nivel = models.IntegerField()
	tipo = models.CharField(choices=CHOICES, max_length=50)