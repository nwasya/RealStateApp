from django.contrib import admin

# Register your models here.
from RE_info.models import Info

#
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['__str__', 'id_num','is_main']





admin.site.register(Info)
