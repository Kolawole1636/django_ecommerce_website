# Generated by Django 3.2.13 on 2022-08-26 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommweb', '0011_remove_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
