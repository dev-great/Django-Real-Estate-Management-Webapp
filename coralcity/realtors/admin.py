from django.contrib import admin

# Register your models here.

from .models import realtor
from django.contrib.auth.models import Group


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'First_name', 'Last_name', 'email', 'hire_date')
    list_display_links = ('id', 'First_name', 'Last_name', 'email')
    search_fields = ('First_name', 'Last_name', 'email')
    list_per_page = 30


admin.site.register(realtor, RealtorAdmin)
