# store/admin.py
from django.contrib import admin
from .models import Brand, CarModel, Year, Product

admin.site.name = 'Modernoo'
admin.site.site_header = 'Modernoo Adminstration'
admin.site.site_header = 'Modernoo Adminstration'
admin.site.site_title = 'SJoj'

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')


admin.site.register(CarModel)
admin.site.register(Year)
admin.site.register(Product)