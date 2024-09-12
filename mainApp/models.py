from django.db import models
from django.utils.safestring import mark_safe


class Goods(models.Model):

    class Meta:
        verbose_name = 'Основные товары'
        verbose_name_plural = 'Основные товары'

    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    photo = models.ImageField(upload_to='goods',
                              blank=True)
    cost = models.DecimalField(
        max_digits=15, decimal_places=2, verbose_name="cost")
    avaliable = models.BooleanField(default=True, verbose_name="avaliable")

    def image_img(self):
        if self.photo:
            return mark_safe(u'<img src="{0}" width="100"/>'.format(self.photo.url))
        else:
            return '(Нет изображения)'
    image_img.short_description = 'PHOTO'
    image_img.allow_tags = True

    def __str__(self):
        return self.name


# Create your models here.
