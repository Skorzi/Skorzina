from django.contrib import admin
from .models import Goods
from django.utils.safestring import mark_safe

@admin.register(Goods)
class GoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo', "image_img", 'cost']
    list_display_links = ('name', )
    list_filter = ('name', 'cost')
    verbose_name = 'Основные товары'
# Register your models here.


admin.site.site_title = 'Skorzina'
admin.site.site_header = 'Skorzina'
