# Generated by Django 3.2.7 on 2022-03-07 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_alter_goods_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='photo',
            field=models.ImageField(blank=True, upload_to='static/mainApp/images/%Y/%m/%d'),
        ),
    ]
