from django.contrib import admin
from .models import Goods
from django.utils.safestring import mark_safe

@admin.register(Goods)
class GoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo', "image_img", 'cost']

# Register your models here.
