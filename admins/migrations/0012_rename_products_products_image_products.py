# Generated by Django 4.1.2 on 2022-10-30 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0011_products_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products_image',
            old_name='products',
            new_name='Products',
        ),
    ]
