from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Plant

# Register Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}

# Register Plant
@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'image_preview')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    prepopulated_fields = {"slug": ("name",)}

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Image'
