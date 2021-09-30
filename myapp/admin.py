from django.contrib import admin

# Register your models here.
from myapp.models import Women,Categories


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id','title','photo','is_published','slug')
    list_display_links = ('id','title',)
    list_editable = ('is_published',)
    search_fields = ('title','content',)
    list_filter = ('time_create','time_update')
    prepopulated_fields = {"slug":("title",)}


class CategorieAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug',)
    list_display_links = ('id',)
    prepopulated_fields = {"slug":("name",)}


admin.site.register(Women,WomenAdmin)
admin.site.register(Categories,CategorieAdmin)
