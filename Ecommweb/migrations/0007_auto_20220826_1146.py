# Generated by Django 3.2.13 on 2022-08-26 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommweb', '0006_auto_20220826_1133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(),
        ),
    ]
