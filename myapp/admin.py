from django.contrib import admin

# Register your models here.
from myapp.models import Women,Categories


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id','title','photo','is_published')
    list_display_links = ('id','title')
    list_editable = ('is_published','photo')
    search_fields = ('title','content')
    list_filter = ('time_create','time_update')


admin.site.register(Women,WomenAdmin)
admin.site.register(Categories)
