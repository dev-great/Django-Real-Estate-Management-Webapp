from django.contrib import admin

# Register your models here.
from .models import Property

class PropertyAdmin(admin.ModelAdmin):
	list_display =('id', 'title', 'city', 'state', 'list_data', 'price','status', 'is_published')
	search_fields = ('name', 'city', 'state',)
	list_display_links = ('title', 'city', 'state', 'price',)
	list_per_page = 50
	list_filter = ('city', 'state', 'price', 'status', 'list_data')


admin.site.register(Property, PropertyAdmin)