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
	animals = models.ForeignKey('Animal', on_delete=models.SET_NULL, null=True, related_name = 'animalAtExhibit', blank=True)
	
	def __str__(self):
		return self.name
		return self.zoo
		return self.animal
		
	def get_absolute_url(self):
		return reverse('exhibitDetail', args=[str(self.id)])
		
class Neighbor(models.Model):
	fromExhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True, related_name = 'fromExhibit')
	direction = models.CharField(max_length=200)
	toExhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True, related_name = 'toExhibit')
	
	def __str__(self):
		return str(self.fromExhibit)
		return self.direction
		return str(self.toExhibit)
	
class Animal(models.Model):
	name = models.CharField(max_length=200, help_text="Enter an Animal Name")
	exhibit = models.ForeignKey('Exhibit', on_delete=models.SET_NULL, null=True, related_name = 'Exhibit', blank=True)
	zoo = models.ForeignKey('Zoo', on_delete=models.SET_NULL, null=True)
	
	def __str__(self):
		return self.name
		return self.zoo
		return self.exhibit
