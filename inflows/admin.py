from django.contrib import admin
from . import models


class InflowAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'product', 'quantity', 'description', 'created_at', 'update_at',)
    search_fields = ('supplier__name','product__title',)
    
    
admin.site.register(models.Inflow, InflowAdmin)