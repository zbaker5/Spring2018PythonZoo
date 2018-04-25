from django.contrib import admin

from .models import Zoo, Exhibit, Animal

# Register your models here.


class ZooAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

admin.site.register(Zoo, ZooAdmin)

class ExhibitAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

admin.site.register(Exhibit, ExhibitAdmin)

class AnimalAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

admin.site.register(Animal, AnimalAdmin)	
