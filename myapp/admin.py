from django.contrib import admin

# Register your models here.
from myapp.models import Women, Categories


class CategorieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    list_filter = ('time_create', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('id', 'title')


admin.site.register(Women, WomenAdmin)
admin.site.register(Categories, CategorieAdmin)
