# Generated by Django 4.1.2 on 2022-10-29 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0007_remove_sub_category_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.sub_category'),
        ),
    ]
