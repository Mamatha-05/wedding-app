from django.contrib import admin
from .models import Wedding,Vendor,select,profile
@admin.register(Wedding)
class WeddingAdmin(admin.ModelAdmin):
    list_display = ['id']
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['id']
@admin.register(select,profile)
class selectAdmin(admin.ModelAdmin):
    list_display = ['id']
