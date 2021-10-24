

from django.contrib import admin

from .models import Property, PropertyImage, Type, Features, Status


class PropertyImageAdmin(admin.StackedInline):
    model = PropertyImage


admin.site.register(Type)
admin.site.register(Features)
admin.site.register(Status)

@admin.register(Property)
class PostAdmin(admin.ModelAdmin):
    inlines = [PropertyImageAdmin]

    class Meta:
        model = Property


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    pass