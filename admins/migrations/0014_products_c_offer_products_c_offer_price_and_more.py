# Generated by Django 4.1.2 on 2022-11-19 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0013_delete_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='c_offer',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='products',
            name='c_offer_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='products',
            name='p_offer',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='products',
            name='p_offer_price',
            field=models.IntegerField(default=0),
        ),
    ]
