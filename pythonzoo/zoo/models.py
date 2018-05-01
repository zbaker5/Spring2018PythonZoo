from django.db import models
from django.urls import reverse

# Create your models here.

class Zoo(models.Model):
	name = models.CharField(max_length=200, help_text="Enter a Zoo Name")
	logoFileName = models.CharField(max_length=200, help_text="Enter the logo file path", null=True)
	
	def __str__(self):
		return self.name
		
	def get_absolute_url(self):
		return reverse('zooDetail', args=[str(self.id)])
	
class Exhibit(models.Model):
	name = models.CharField(max_length=200, help_text="Enter a Exhibit Name")
	zoo = models.ForeignKey('Zoo', on_delete=models.SET_NULL, null=True)
	
	def __str__(self):
		return self.name
		return self.zoo
		return self.animal
		
	def get_absolute_url(self):
		return reverse('exhibitDetail', args=[str(self.id)])
	
class Animal(models.Model):
	name = models.CharField(max_length=200, help_text="Enter an Animal Name")
	imageFileName = models.CharField(max_length=200, help_text="Enter the image file path", null=True)
	soundFileName = models.CharField(max_length=200, help_text="Enter the sound file path", null=True)
	exhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True, related_name = 'Exhibit', blank=True)
	zoo = models.ForeignKey('Zoo', on_delete=models.SET_NULL, null=True)
	habitatDescription = models.CharField(max_length=200, help_text="Enter a description of the habitat.", null=True)
	dietDescription = models.CharField(max_length=200, help_text="Enter a description of the animal's diet.", null=True)
	
	def __str__(self):
		return self.name
		return self.zoo
		return self.exhibit
		
	def get_absolute_url(self):
		return reverse('animalDetail', args=[str(self.id)])	
		
class ExhibitNeighbor(models.Model):
	fromExhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True, related_name = 'fromExhibit')
	toExhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True, related_name = 'toExhibit')
	
	CARDINAL = (
		('n', 'North'),
		('s', 'South'),
		('w', 'West'),
		('e', 'East'),
		('nw', 'NorthWest'),
		('ne', 'NorthEast'),
		('sw', 'SouthWest'),
		('se', 'SouthEast')
	)
	
	direction = models.CharField(max_length=2, choices=CARDINAL, help_text='Enter Direction', null=True, blank=True)
	
	def __str__(self):
		return str(self.fromExhibit)
		return self.direction
		return str(self.toExhibit)
	

