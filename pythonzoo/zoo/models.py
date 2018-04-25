from django.db import models

# Create your models here.

class Zoo(models.Model):
	name = models.CharField(max_length=200, help_text="Enter a Zoo Name")
	
	def __str__(self):
		return self.name
	
class Exhibit(models.Model):
	name = models.CharField(max_length=200, help_text="Enter a Exhibit Name")
	zoo = models.ForeignKey('Zoo', on_delete=models.SET_NULL, null=True)
	
	def __str__(self):
		return self.name
		
class ExhibitNeighbors(models.Model):
	#fromExhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True)
	direction = models.CharField(max_length=200)
	#toExhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True)
	
class Animal(models.Model):
	name = models.CharField(max_length=200, help_text="Enter an Animal Name")
	exhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True)
	
	def __str__(self):
		return self.name
