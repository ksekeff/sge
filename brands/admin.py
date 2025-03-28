from django.contrib import admin
from .models import Brand

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)  # Sempre uma tupla
    search_fields = ('name',)

admin.site.register(Brand, BrandAdmin)