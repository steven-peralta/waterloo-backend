# Generated by Django 2.1.5 on 2019-02-09 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20190207_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, height_field='image_width', upload_to='blog/%Y/%m/%d', width_field='image_height'),
        ),
    ]