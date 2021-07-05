from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
	list_display = ('id' , 'name' , 'listing' , 'email' , 'contact_date' )
	list_display_links = ('id' , 'name')
	search_fields = ('email','listing')
	list_filter = ( 'contact_date',)
	list_per_page = 50



# Register your models here.
admin.site.register(Contact , ContactAdmin)
