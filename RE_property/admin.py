

from django.contrib import admin

from .models import Property, PropertyImage


class PropertyImageAdmin(admin.StackedInline):
    model = PropertyImage




@admin.register(Property)
class PostAdmin(admin.ModelAdmin):
    inlines = [PropertyImageAdmin]

    class Meta:
        model = Property


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    pass