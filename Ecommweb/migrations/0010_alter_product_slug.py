# Generated by Django 3.2.13 on 2022-08-26 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommweb', '0009_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='products'),
        ),
    ]