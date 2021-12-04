from django.contrib import admin
from .models import AgesVerification

# Register your models here.
class AGISVerificationAdmin(admin.ModelAdmin):
	list_display = ('id' , 'name' , 'email' , 'phone' , 'upload_date')
	list_display_links = ('id' , 'name' , 'email' , 'phone' , )
	list_filter = ('id' , 'name' , 'email' , 'phone' , 'upload_date' )
	search_fields = ('id' , 'name' , 'email' , 'phone' , 'upload_date')
	list_per_page = 15


# Register your models here.
admin.site.register(AgesVerification, AGISVerificationAdmin)
