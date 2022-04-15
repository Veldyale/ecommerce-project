# Generated by Django 3.2.6 on 2022-04-11 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.PositiveIntegerField(default=1, max_length=10, unique=True, verbose_name='phone'),
            preserve_default=False,
        ),
    ]
