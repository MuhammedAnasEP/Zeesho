# Generated by Django 4.1.2 on 2022-10-29 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0008_alter_products_sub_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='sub_category',
            field=models.CharField(max_length=50),
        ),
    ]
