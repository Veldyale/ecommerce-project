# Generated by Django 3.2.6 on 2021-08-31 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20210831_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_1',
            field=models.ImageField(blank=True, upload_to='product_1'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_2',
            field=models.ImageField(blank=True, upload_to='product_2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_3',
            field=models.ImageField(blank=True, upload_to='product_3'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_4',
            field=models.ImageField(blank=True, upload_to='product_4'),
        ),
    ]
