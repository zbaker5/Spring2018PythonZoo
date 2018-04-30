from django.contrib import admin

from .models import Zoo, Exhibit, Animal, Neighbor

# Register your models here.


class ZooAdmin(admin.ModelAdmin):
	list_display = ('name', 'id', 'logoFileName', 'get_absolute_url')

admin.site.register(Zoo, ZooAdmin)

class ExhibitAdmin(admin.ModelAdmin):
	list_display = ('name', 'zoo', 'animals', 'get_absolute_url', 'id')

admin.site.register(Exhibit, ExhibitAdmin)

class AnimalAdmin(admin.ModelAdmin):
	list_display = ('name', 'exhibit', 'zoo', 'id')

admin.site.register(Animal, AnimalAdmin)	

class NeighborAdmin(admin.ModelAdmin):
	list_display = ('toExhibit', 'fromExhibit', 'direction', 'id')
	
admin.site.register(Neighbor, NeighborAdmin)
