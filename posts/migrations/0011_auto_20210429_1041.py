# Generated by Django 3.2 on 2021-04-29 05:41

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20210427_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannermodel',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '720x480', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
        migrations.AlterField(
            model_name='gallerymodel',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '400x250', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
        migrations.AlterField(
            model_name='gallerymodel',
            name='image',
            field=models.ImageField(upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '720x480', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='description',
            field=models.TextField(max_length=450, null=True),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='image',
            field=models.ImageField(upload_to='news'),
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '720x480', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='image',
            field=models.ImageField(upload_to='staff'),
        ),
    ]